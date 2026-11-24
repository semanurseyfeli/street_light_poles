# Zeche Zollern Benchmark Dataset

This folder contains the object detection annotations for the Zeche Zollern area, Dortmund, Germany.

The annotations were prepared for detecting street light pole configurations in single nadir-viewing aerial image using the YOLO format.

## Dataset Structure

The dataset is organized into the following subfolders:

- **test/**: Contains the YOLO-format annotation file for the test image.
- **results/**: Contains the 3D-reconstructed street light pole results for the test image in PLY format.

## Object Classes

| Class ID | Class Name |
|:---:|---|
| 0 | Single-arm |
| 1 | Double-arm |

## Data Availability

The test annotation is provided in YOLO format (`.txt`). The corresponding aerial image is not included in this repository.
