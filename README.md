# 3D Reconstruction of Street Light Poles from Single Nadir-Viewing Aerial Imagery and Digital Terrain Model

This repository contains the annotations and resources associated with a research study on street light poles using aerial imagery. The repository includes data from two study areas in Dortmund, Germany: Dortmund City Center and Zeche Zollern [1]. It covers different street light pole configurations, including single-arm and double-arm poles.

## Datasets

Two study areas are included in this repository:

- **Dortmund City Center:** YOLO-format annotations for the training,validation and test sets; binary masks for image footprint masking in the training and validation sets; and a python script for image and annotation processing.
- **Zeche Zollern:** YOLO-format test annotations.

## Object Classes

| Class ID | Class Name |
|:---:|---|
| 0 | Single-arm |
| 1 | Double-arm |

## Data Sources and Acknowledgements

The aerial imagery used in this study was obtained from the following sources:

- **Dortmund City Center:** The aerial imagery is part of the ISPRS/EuroSDR Dortmund benchmark dataset. Further information, registration, and access details are available through the [ISPRS Benchmark website](https://www2.isprs.org/commissions/comm2/icwg-2-1a/benchmark_main/data-description-image-orientation/).

- **Zeche Zollern:** The aerial imagery is part of the ISPRS/EuroSDR Dortmund benchmark dataset. Further information and access details are available through the [ISPRS Benchmark website](https://www2.isprs.org/commissions/comm2/icwg-2-1a/benchmark_main/description_dortmund/).

The original aerial images are not included in this repository. This repository provides the annotations and related resources generated for this study.
## How to Cite

Users of the datasets, annotations, and other resources provided in this repository are kindly requested to cite the following publication:

Seyfeli, S., & Ok, A. O. (2026). 3D Reconstruction of Street Light Poles from Single Nadir-Viewing Aerial Imagery and Digital Terrain Model. *Remote Sensing* (under review).

Please also acknowledge the benchmark data providers as required by the dataset terms of use.

## License

The datasets are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) license. The Python script is released under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0/).

## References

[1] Nex, F., Gerke, M., Remondino, F., Przybilla, H.-J., Bäumker, M., & Zurhorst, A. (2015). ISPRS Benchmark for Multi-Platform Photogrammetry. *ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences*, II-3/W4, 135–142. https://doi.org/10.5194/isprsannals-II-3-W4-135-2015
