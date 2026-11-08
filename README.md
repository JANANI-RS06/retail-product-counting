# AI-Based Retail Product Counting and Stock Reconciliation

An AI-powered computer vision project that detects and counts products from retail shelf images and supports automated inventory reconciliation.

## Project Overview

This project uses a YOLO-based ONNX object detection model to identify retail products in shelf images. It supports single-image detection, batch processing, stock reconciliation, confidence analysis, and data visualization.

## Key Features

- Retail product detection using a pretrained ONNX model
- Automated product counting
- Batch processing of multiple shelf images
- Bounding-box visualization
- Stock reconciliation (Over-count, Under-count, Matched)
- CSV report generation
- Confidence threshold comparison
- Detection result dashboards and charts

## Technologies Used

- Python
- ONNX Runtime
- OpenCV
- NumPy
- Pandas
- Matplotlib
- YOLO-based object detection
- Visual Studio Code

## Project Status

**In Progress – Prototype Implementation and Testing**


## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd retail-product-counting
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install ultralytics opencv-python pandas numpy matplotlib onnxruntime onnx
```

### 5. Model Setup

Place the retail object detection ONNX model in the project root directory.

Model filename:

`sku110k-yolo11-n640.onnx`


## How to Run

1. Single Image Detection

```bash
python retail_detection.py

2. Stock Reconciliation
python stock_reconciliation.py

3. Generate Dashboard
python visualization.py

4. Run Complete Workflow
python main.py

5. Batch Product Detection
python batch_detection.py

6. Generate Batch Summary
python batch_summary.py

7. Batch Visualization
python batch_visualization.py

8. Confidence Analysis
python confidence_analysis.py

9. Confidence Visualization
python confidence_visualization.py

10. Threshold Comparison
python threshold_comparison.py

## Experimental Results

### Batch Detection

| Shelf Image | Detected Products |
|---|---:|
| shelf1.jpg | 86 |
| shelf2.webp | 199 |
| shelf3.webp | 214 |
| **Total** | **499** |

### Confidence Threshold Comparison

| Metric | Threshold 0.25 | Threshold 0.40 |
|---|---:|---:|
| Total detections | 499 | 367 |

Increasing the confidence threshold from 0.25 to 0.40 reduced accepted detections by 132 (26.45%).

### Confidence Analysis

| Shelf Image | Average Confidence |
|---|---:|
| shelf1.jpg | 48.9% |
| shelf2.webp | 54.9% |
| shelf3.webp | 51.9% |

**Note:** Detection counts are model predictions, not verified actual product counts. Ground-truth annotations are required to evaluate detection accuracy.

## Limitations

- Detection performance depends on image quality and lighting conditions.
- Overlapping products may cause missed or duplicate detections.
- Current implementation uses CPU-based inference.
- Actual detection accuracy has not yet been verified using ground-truth annotations.
- Direct image resizing may distort product proportions.

## Future Enhancements

- Fine-tune the detection model using retail-specific datasets.
- Improve image preprocessing and detection performance.
- Integrate real-time camera-based product detection.
- Add barcode scanning for inventory verification.
- Integrate a database for stock management.
- Evaluate performance using Precision, Recall, and mAP.
- Explore GPU acceleration.

## Project Status

Prototype implementation and testing completed. Further model evaluation and optimization are planned.

## Author

**Janani RS**

B.Tech – Artificial Intelligence and Data Science