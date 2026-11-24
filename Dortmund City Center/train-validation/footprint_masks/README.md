# footprint_masks

This folder contains the binary masks generated for the overlapping aerial images in the Dortmund City Centre dataset.
The masks identify image regions corresponding to the reference footprint (005_010_163000209.tif) and are used during the preparation of the train/validation datasets.

The binary masks are stored in png format and have the same spatial dimensions as their corresponding aerial images.

| Pixel Value | Meaning |
|---|---|
| 0  | Unmasked region |
| 1 | Masked region   |

The masks are used to identify regions that should be excluded from the training and validation data. The corresponding YOLO annotations should be updated accordingly:

- Bounding boxes entirely within masked regions should be removed.
- Bounding boxes partially overlapping masked regions should be adjusted based on the remaining unmasked pixels.
- Bounding boxes outside masked regions should be retained.

Each mask corresponds to an aerial image and uses the same filename to facilitate image-mask matching.
