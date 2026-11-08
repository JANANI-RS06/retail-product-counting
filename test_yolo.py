from ultralytics import YOLO
import torch

print("Loading pretrained YOLO26n model...")

model = YOLO("yolo26n.pt")

print("YOLO model loaded successfully!")

print("CUDA Available:", torch.cuda.is_available())

print("\nSupported detection classes:")
print(model.names)

print("\nProject setup completed!")