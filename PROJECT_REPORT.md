# AI-Based Retail Product Counting and Stock Reconciliation

## 1. Project Overview

The AI-Based Retail Product Counting and Stock Reconciliation system is designed to automate product detection and counting in retail shelf images using computer vision and deep learning.

The system uses a YOLO-based ONNX object detection model to identify products from shelf images. It processes individual and multiple images, counts detected products, and compares the detected quantity with the expected stock quantity.

The project also generates CSV reports and visual dashboards to help understand detection results and inventory differences.

## 2. Problem Statement

Manual product counting in retail stores is time-consuming and can lead to human errors.

Traditional inventory checking requires employees to physically count products on shelves and compare them with available stock records.

This project aims to develop an automated image-based product counting system to support retail inventory monitoring.

## 3. Project Objectives

The main objectives of this project are:

1. To detect retail products from shelf images using deep learning.
2. To automate product counting using computer vision.
3. To process multiple shelf images in a single execution.
4. To compare detected product counts with expected stock quantities.
5. To identify over-counting and under-counting situations.
6. To generate CSV-based detection and inventory reports.
7. To visualize product detection results using charts.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| YOLO-based ONNX Model | Retail product detection |
| ONNX Runtime | Model inference |
| OpenCV | Image processing and bounding boxes |
| NumPy | Numerical operations |
| Pandas | Data analysis and CSV processing |
| Matplotlib | Data visualization |
| VS Code | Development environment |

## 5. Project Workflow

The system follows the workflow below:

1. Input Image: Retail shelf images are provided as input.
2. Image Preprocessing: Images are resized to 640 × 640 pixels and converted into the required model input format.
3. Model Inference: The ONNX-based object detection model processes the images.
4. Confidence Filtering: Predictions below the selected confidence threshold are removed.
5. Non-Maximum Suppression: Overlapping bounding boxes are filtered.
6. Product Counting: Remaining detections are counted.
7. Stock Reconciliation: Detected quantity is compared with expected stock.
8. Report Generation: Detection and reconciliation results are saved as CSV files.
9. Visualization: Charts are generated to summarize the results.


## 6. Implementation Modules

### 6.1 Image-Based Product Detection
Uses an ONNX object detection model to identify retail products from shelf images.

### 6.2 Batch Detection
Processes multiple shelf images in one execution and generates bounding-box result images.

### 6.3 Stock Reconciliation
Compares detected product quantities with expected stock quantities and identifies:
- Matched Stock
- Over-count
- Under-count

### 6.4 CSV Report Generation
Stores detection details, confidence scores, bounding-box coordinates, and stock reconciliation results.

### 6.5 Data Visualization
Generates charts to visualize product counts, stock differences, batch detection results, and confidence scores.

### 6.6 Confidence Threshold Analysis
Compares detection results using confidence thresholds of 0.25 and 0.40.


## 7. Experimental Results

The system was tested using three retail shelf images.

### 7.1 Batch Detection Results

| Test Image | Detected Products |
|---|---:|
| shelf1.jpg | 86 |
| shelf2.webp | 199 |
| shelf3.webp | 214 |
| Total | 499 |

### 7.2 Confidence Threshold Comparison

Two confidence thresholds were evaluated.

| Test Image | Threshold 0.25 | Threshold 0.40 |
|---|---:|---:|
| shelf1.jpg | 86 | 52 |
| shelf2.webp | 199 | 148 |
| shelf3.webp | 214 | 167 |
| Total | 499 | 367 |

Increasing the confidence threshold from 0.25 to 0.40 reduced the total number of detections by 132 (approximately 26.45%).

### 7.3 Confidence Analysis

| Test Image | Average Confidence |
|---|---:|
| shelf1.jpg | 48.9% |
| shelf2.webp | 54.9% |
| shelf3.webp | 51.9% |

Note: These values represent model predictions. They do not establish actual detection accuracy because manually verified ground-truth annotations have not yet been prepared.


## 8. Limitations

1. Detection results depend on image quality and lighting conditions.
2. Overlapping products may lead to missed or duplicate detections.
3. The current implementation uses CPU-based inference.
4. The model has not yet been evaluated using manually verified ground-truth annotations.
5. Direct image resizing may distort product proportions.

## 9. Future Enhancements

1. Train and fine-tune the detection model using a retail-specific dataset.
2. Improve detection accuracy through proper image preprocessing.
3. Add support for real-time camera-based product detection.
4. Integrate barcode scanning for improved inventory verification.
5. Develop a database for maintaining inventory records.
6. Evaluate model performance using Precision, Recall, and mAP.
7. Optimize inference speed using GPU acceleration.

## 10. Conclusion

The AI-Based Retail Product Counting and Stock Reconciliation project demonstrates an automated approach to retail shelf product detection and inventory monitoring.

The system successfully performs image-based detection, batch processing, product counting, stock reconciliation, CSV report generation, and visualization.

The threshold comparison demonstrates how confidence filtering affects the number of accepted detections.

This prototype provides a foundation for developing more accurate and scalable AI-powered retail inventory management systems.