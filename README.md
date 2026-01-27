# Hierarchy to Beat Perception in Two Modalities of Audition and Vision

This repository contains the code, data (sample and derived), and analysis pipelines used in the PhD project **Duration, Sequence, and Beat Perception across Modalities**.  
The project investigates how lower-level timing abilities contribute to beat perception across auditory and visual modalities.

## Repository structure

- `experiment/`  
  PsychoPy experiment code and stimuli used to collect behavioral data from participants.  
  See `experiment/README.md` for full experimental details and instructions.

- `data/`  
  Raw (not shared), sample, and derived datasets, along with documentation describing data availability and generation.  
  See `data/README.md` for details.

- `raw_to_preprocessed/`  
  Scripts used to preprocess raw data files into preprocessed files.
  See `raw_to_preprocessed/README.md` for details.

- `preprocessed_to_xlsx/`  
  Scripts for converting preprocessed data into structured formats used in downstream analyses.
  See `preprocessed_to_xlsx/README.md` for details.

- `survey_analysis`
  Script for deriving information of interest from the end-of-study questionnaire responses.

- `results/`
  xlsx files containing questionnaire results as well as group-level and clustering results.
  See `results/README.md` for details.

- `clustering_analysis/`  
  Clustering analyses (silhouette analysis and k-means) used to group participants based on performance.
  See `clustering_analysis/README.md` for details.

- `visualization/`  
  Code for generating figures and visualizations.

- `plots/`  
  Generated plots and figures used in analyses and manuscripts.

## Data availability

Full raw experimental and questionnaire data are not publicly shared due to participant privacy considerations.  
Sample data and all preprocessing and analysis code are provided to support reproducibility.

## Citation

If you use this repository, please cite:

> Mohammad Alipour, Z., Butler, B., & Grahn, J. (2024).  
> *Duration, Sequence, and Beat Perception across Modalities*.  
> Preprint available at: https://osf.io/preprints/psyarxiv/yqbhc_v1

## License

This project is released under the MIT License.

## Contact

**Zhaleh Mohammad Alipour**  
📧 zhaleh.m.alipour@gmail.com