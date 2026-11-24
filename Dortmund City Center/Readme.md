# Dortmund City Center Dataset

This folder contains the street light pole object detection dataset for the Dortmund City Center, Germany.
The dataset was prepared for detecting street light pole configurations in nadir-viewing aerial images using the YOLO format.

## Dataset Structure

The dataset is organized into the following subfolders:

- **train-validation/**: Contains the image and annotation splitting code, YOLO-format annotation files and binary footprint masks for the train/validation images.
- **test/**: Contains the YOLO-format annotation file for the test image.

## Object Classes

| Class ID | Class Name |
|:---:|---|
| 0 | Single-arm |
| 1 | Double-arm |

## Annotation Format
The annotations follow the YOLO format, where each object is represented by five values:
```text
class_id x_center y_center width height
```

## Data Availability

The train-validation folders contain annotation files and their corresponding binary overlap masks. The test folder contains only the annotation file. The corresponding aerial images are not included in this repository.
