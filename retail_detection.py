import cv2
import onnxruntime as ort
import numpy as np
import csv

MODEL_PATH = "sku110k-yolo11-n640.onnx"
IMAGE_PATH = "test_images/retail_shelf.webp"

print("Loading retail model...")

session = ort.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)

# Read image
image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError("Shelf image not found!")

original_height, original_width = image.shape[:2]
print("Image dimensions:", image.shape)
print("Original image width:", original_width)
print("Original image height:", original_height)

# Resize and prepare image
resized = cv2.resize(image, (640, 640))
rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

input_data = rgb.astype(np.float32) / 255.0
input_data = np.transpose(input_data, (2, 0, 1))
input_data = np.expand_dims(input_data, axis=0)

# Run model
input_name = session.get_inputs()[0].name
outputs = session.run(None, {input_name: input_data})

predictions = outputs[0][0].T

print("Model inference completed!")
print("Prediction shape:", predictions.shape)

# Confidence filtering
confidence_threshold = 0.25
valid_predictions = predictions[
    predictions[:, 4] >= confidence_threshold
]

print("Detections before NMS:", len(valid_predictions))

# Convert bounding boxes to OpenCV format
boxes = []
scores = []

for prediction in valid_predictions:
    x, y, w, h, confidence = prediction

    x1 = int((x - w / 2) * original_width / 640)
    y1 = int((y - h / 2) * original_height / 640)
    box_width = int(w * original_width / 640)
    box_height = int(h * original_height / 640)

    boxes.append([x1, y1, box_width, box_height])
    scores.append(float(confidence))

# Remove duplicate overlapping boxes
indices = cv2.dnn.NMSBoxes(
    boxes,
    scores,
    confidence_threshold,
    0.45
)

total = len(indices)

for i in indices:
    x, y, w, h = boxes[int(i)]
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

print("\nTotal products detected:", total)

cv2.imwrite("retail_result.jpg", image)
# Save detection results to CSV
with open("product_counts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Product_ID",
        "Confidence",
        "X",
        "Y",
        "Width",
        "Height"
    ])

    for product_id, i in enumerate(indices, start=1):
        x, y, w, h = boxes[int(i)]

        writer.writerow([
            product_id,
            round(scores[int(i)], 3),
            x, y, w, h
        ])

print("CSV report saved as product_counts.csv")

print("Result saved as retail_result.jpg")