# Image and Annotation Cropping

This folder contains a Python script (`clip_images.py`) for dividing large aerial images into smaller image tiles and updating their corresponding YOLO-format annotations.

The script processes TIFF images and their associated annotation files. Each image is divided into non-overlapping tiles, and the object bounding boxes are clipped to the boundaries of each tile. The resulting bounding boxes are converted into YOLO format and saved along with the corresponding image tiles.

## Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Input Data

The script requires two inputs, which must be provided by the user when running the script.

**1. Aerial Images**

The user must provide the local directory containing the input aerial images in TIFF format.

**2. Annotations**

The user must provide the local directory containing the corresponding YOLO-format annotation files.

Each annotation file must have the same filename as its corresponding image and use the `.txt` extension.

The annotation format is:

```text
class_id x_center y_center width height
```

## Masked Input Data

For this study, the image slicing process is applied to masked aerial images and their corresponding annotations.

The `footprint_masks/` directory contains binary masks for the aerial images. These masks are provided to support the image masking process. Users must apply the corresponding binary masks to the aerial images and update the full-size YOLO-format annotations accordingly before running the slicing script.

The `annotations/` directory contains the bounding boxes for the full-size aerial images.

The following conditions must be met before running the script:

- The input aerial images must be masked using the corresponding binary masks.
- The annotation files must be updated consistently with the masked images.
- Annotations belonging to excluded or masked objects must be removed or adjusted accordingly.
- Each image must have a corresponding annotation file with the same filename.

## Configuration

The slicing parameters are defined in the Python script:

| Parameter | Value | Description |
|---|---:|---|
| Slice size | 640 × 640 pixels | Dimensions of each image tile |
| Overlap ratio | 0 | No overlap between adjacent tiles |
| Step size | 640 pixels | Distance between consecutive tiles |

## Usage

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Run the script:

```bash
python clip_images.py
```

3. When prompted, provide the local directory containing the masked aerial images.
4. Provide the local directory containing the corresponding masked annotation files.

## Output

The script automatically creates the following output directory structure in the same directory as the Python script:

```text
train-validation/
└── sliced_data/
    ├── images/
    └── labels/
```

- **images/**: Contains the generated image tiles in TIFF format.
- **labels/**: Contains the updated YOLO-format annotation files corresponding to the generated image tiles.

Each output image and its annotation file share the same filename.

Only tiles containing at least one annotated object are retained.

## Notes

- The original images and annotation files are not modified.
- Input images and annotations are read from user-specified local directories.
- Generated image tiles and annotations are saved locally.
- The script does not perform masking. It reads the full-size image annotations, clips the bounding boxes to the boundaries of each image tile, and converts them into YOLO format relative to the tile dimensions.


