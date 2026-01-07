# Clustering_analysis

This folder contains the code used for clustering analyses of participant performance data.

The clustering pipeline consists of two main steps:  
(1) selection of the optimal number of clusters, and  
(2) assignment of participants to clusters.

## Folder structure

### Silhouette_plots/
This folder contains scripts used to perform silhouette analysis for different sensory modalities.

Silhouette plots were used to evaluate clustering solutions with different numbers of clusters and to determine the optimal value of *k* for each modality.  
The theoretical background and methodological details of silhouette analysis are described in the online manuscript.

> Mohammad Alipour, Z., Butler, B., & Grahn, J (2024). *Duration, Sequence, and Beat Perception across Modalities*. Preprint available at: https://osf.io/preprints/psyarxiv/yqbhc_v1

### k-means/
This folder contains scripts that perform k-means clustering using the selected number of clusters.

Separate scripts are provided for:
- auditory modality
- visual modality

These scripts assign each participant to a specific cluster and generate CSV files for visualization.

## Outputs

The k-means scripts generate the following files:

- `Three_Auditory_Clusters.csv`  
  Used for creating scatter plots

- `Three_Auditory_Clusters_2.csv`  
  Used for creating bar plots

- `Two_Visual_Clusters.csv`  
  Used for creating scatter plots

- `Two_Visual_Clusters_2.csv`  
  Used for creating bar plots

All generated CSV files are stored in the `results/` folder.  
The corresponding plots are stored in the `plots/` folder.

