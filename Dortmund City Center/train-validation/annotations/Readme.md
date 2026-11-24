# Annotations
This folder contains full-image annotations in YOLO format for street light pole objects in the Dortmund City Center dataset.

The annotations correspond to the original full-size aerial image. They are intended to be used as input for the image masking and slicing procedures.

The annotations must be updated consistently with the corresponding binary image masks before the slicing process.

## Object Classes
| Class ID | Class Name |
|---|---|
| 0 | Single-arm |
| 1 | Double-arm |

## Annotation Format
The annotations are provided as `.txt` files. Each annotation file corresponds to an image with the same filename.
Each object is represented by five values:

```text
class_id x_center y_center width height
```

## File Naming
Each annotation file has the same filename as its corresponding image, with a `.txt` extension.

