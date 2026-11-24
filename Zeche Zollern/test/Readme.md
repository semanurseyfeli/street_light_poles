# Test Annotation

This folder contains the YOLO-format annotation file for a single nadir-view test image from the Zeche Zollern benchmark dataset, Dortmund, Germany.

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

The annotation file is provided in `.txt` format and corresponds to the test image with the same filename.

## Data Availability

Only the annotation file is provided in this folder. The corresponding aerial image is not included.

