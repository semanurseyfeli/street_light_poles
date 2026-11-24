# Copyright (c) 2026 Semanur Seyfeli
# Licensed under the PolyForm Noncommercial License 1.0.0 (Non-commercial use only).
# Full license text: https://polyformproject.org
# Citation required: Please cite this repository if you use this code.

import os
import cv2
import numpy as np
from pathlib import Path

# Directory containing this script
base_dir = Path(__file__).resolve().parent

# User-provided image directory
image_dir = Path(
    input("Enter image directory: ").strip().strip('"')
)

# User-provided annotation directory
label_dir = Path(
    input("Enter annotation directory: ").strip().strip('"')
)

# Output directories
output_dir = base_dir / "sliced_data"
output_image_dir = output_dir / "images"
output_label_dir = output_dir / "labels"

# Check input directories
if not image_dir.is_dir():
    raise FileNotFoundError(f"Image directory not found: {image_dir}")

if not label_dir.is_dir():
    raise FileNotFoundError(f"Annotation directory not found: {label_dir}")

# Create output directories
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

slice_size = 640
overlap_ratio = 0
step_size = int(slice_size * (1 - overlap_ratio))

os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

def slice_image_and_labels(img_path, label_path):
    img = cv2.imread(str(img_path), cv2.IMREAD_UNCHANGED)

    if img is None:
        print(f"Error: {img_path} ")
        return

    h, w = img.shape[:2]
    img_name = img_path.stem

    labels = []
    if label_path.exists():
        with open(label_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) < 5: continue
                cls, x, y, nw, nh = map(float, parts)
                labels.append([
                    int(cls),
                    (x - nw / 2) * w, (y - nh / 2) * h,  # x1, y1
                    (x + nw / 2) * w, (y + nh / 2) * h  # x2, y2
                ])

    for y in range(0, h - step_size + 1, step_size):
        for x in range(0, w - step_size + 1, step_size):
            y2 = min(y + slice_size, h)
            x2 = min(x + slice_size, w)
            y1 = max(0, y2 - slice_size)
            x1 = max(0, x2 - slice_size)

            slice_img = img[y1:y2, x1:x2]
            slice_name = f"{img_name}_{y1}_{x1}"

            slice_labels = []
            for cls, gx1, gy1, gx2, gy2 in labels:
                ix1 = max(gx1, x1)
                iy1 = max(gy1, y1)
                ix2 = min(gx2, x2)
                iy2 = min(gy2, y2)

                if ix2 > ix1 and iy2 > iy1:
                    obj_w = ix2 - ix1
                    obj_h = iy2 - iy1

                    cx = (ix1 + obj_w / 2 - x1) / slice_size
                    cy = (iy1 + obj_h / 2 - y1) / slice_size
                    nw = obj_w / slice_size
                    nh = obj_h / slice_size

                    cx, cy = np.clip([cx, cy], 0, 1)
                    nw, nh = np.clip([nw, nh], 0, 1)

                    slice_labels.append(f"{cls} {cx:.6f} {cy:.6f} {nw:.6f} {nh:.6f}")

            if len(slice_labels) > 0:
                cv2.imwrite(os.path.join(output_image_dir, f"{slice_name}.tif"), slice_img)
                with open(os.path.join(output_label_dir, f"{slice_name}.txt"), "w") as f:
                    f.write("\n".join(slice_labels))


image_extensions = ("*.tif", "*.tiff")
image_files = []
for ext in image_extensions:
    image_files.extend(list(Path(image_dir).glob(ext)))

for img_p in image_files:
    lbl_p = Path(label_dir) / (img_p.stem + ".txt")
    slice_image_and_labels(img_p, lbl_p)
    print(f"Finished: {img_p.name}")

