from ultralytics import YOLO

print("Loading YOLO model...")

model = YOLO("yolo26n.pt")

image_path = "test_images/retail_shelf.jpg"

print("Detecting products...")

results = model.predict(
    source=image_path,
    conf=0.25,
    imgsz=640,
    device="cpu"
)

counts = {}

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        counts[class_name] = counts.get(class_name, 0) + 1

    result.save(filename="retail_detection_result.jpg")

print("\nDetection Results:")

for name, count in counts.items():
    print(name, ":", count)

print("\nTotal detected objects:", sum(counts.values()))
print("Detection completed!")