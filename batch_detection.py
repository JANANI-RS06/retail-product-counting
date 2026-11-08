import cv2
import onnxruntime as ort
import numpy as np
import csv
import os

MODEL_PATH = "sku110k-yolo11-n640.onnx"
IMAGE_FOLDER = "test_dataset"

CONFIDENCE = 0.25
IOU_THRESHOLD = 0.45

print("Loading retail detection model...")

session = ort.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)

input_name = session.get_inputs()[0].name

image_extensions = (".jpg", ".jpeg", ".png", ".webp")
image_files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(image_extensions)
]

all_results = []

for filename in image_files:

    image_path = os.path.join(IMAGE_FOLDER, filename)
    image = cv2.imread(image_path)

    if image is None:
        print("Unable to read:", filename)
        continue

    height, width = image.shape[:2]

    resized = cv2.resize(image, (640, 640))
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    input_data = rgb.astype(np.float32) / 255.0
    input_data = np.transpose(input_data, (2, 0, 1))
    input_data = np.expand_dims(input_data, axis=0)

    outputs = session.run(
        None,
        {input_name: input_data}
    )

    predictions = outputs[0][0].T

    valid = predictions[
        predictions[:, 4] >= CONFIDENCE
    ]

    boxes = []
    scores = []

    for prediction in valid:
        x, y, w, h, confidence = prediction

        x1 = int((x - w / 2) * width / 640)
        y1 = int((y - h / 2) * height / 640)
        box_w = int(w * width / 640)
        box_h = int(h * height / 640)

        boxes.append([x1, y1, box_w, box_h])
        scores.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(
        boxes,
        scores,
        CONFIDENCE,
        IOU_THRESHOLD
    )

    count = len(indices)

    for product_id, i in enumerate(indices, start=1):
        x, y, w, h = boxes[int(i)]

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        all_results.append([
            filename,
            product_id,
            round(scores[int(i)], 3),
            x, y, w, h
        ])

    output_name = f"result_{os.path.splitext(filename)[0]}.jpg"
    cv2.imwrite(output_name, image)

    print(f"{filename} -> {count} products detected")

# Save combined CSV
with open("batch_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Image_Name",
        "Product_ID",
        "Confidence",
        "X", "Y", "Width", "Height"
    ])

    writer.writerows(all_results)

print("\nBatch detection completed!")
print("Total images processed:", len(image_files))
print("Total detections:", len(all_results))
print("CSV saved as batch_results.csv")