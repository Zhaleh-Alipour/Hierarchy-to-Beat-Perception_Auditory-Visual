# Results

This folder contains outputs from different analyses or questionnaires performed in the project.

## end_of_study_Q.xlsx

- **Description:**  
  After the end of the experiment, participants completed an online questionnaire created on Qualtrics that included biographical, music-related, and experiment-related questions.

- **Input:**  
  The original Excel file "data/End_of_study_questionnaire_101.xlsx" containing all participants’ raw questionnaire responses.

- **Analysis:**  
  A preprocessing step was applied to the raw questionnaire data to extract variables of interest. This analysis is saved in end_of_study_questionnaire/Qualtrics analysis.py. The processed information was then compiled and saved into a cleaned output file.

- **Output:**  
  `end_of_study_Q.xlsx` — this file contains the variables required for inclusion in the final report/paper.

- **Notes:**  
  - Columns with labels such as `(>=5 -> 2)` indicate categorical encoding, where:
    - values **less than 5 years** are encoded as `1`
    - values **5 years or more** are encoded as `2`
  - The `unique_id` column represents the unique identifier assigned to each participant.

---

## predicted_results.xlsx

- **Description:**  
  This file contains synthetic data generated to visualize the four predicted patterns of performance expected after running the experiment.

- **Purpose:**  
  The synthetic dataset is used solely for visualization and illustration of expected outcome patterns, not for statistical analysis of real participant data.

- **Visualization code:**  
  `visualization/predicted_results.ipynb`

- **Output plot:**  
  `plots/predicted_results.png`

---

## PrimaryResults_132participants.xlsx

- **Description:**  
  This file contains the main results from all participants included in the study (**N = 132**).

- **Columns 2–7: Block-wise performance with detailed annotations**  
  These columns report participant performance across the six experimental blocks.

  Block labels:
  - **SD** = Single Duration  
  - **Irreg** = Irregular (non-beat)  
  - **Reg** = Regular (beat)

  Data are presented in the following format: 0.79 [0] (0) {2}
where:
- `0.79` → mean performance for that block (per participant)
- `[ ]` → number of **attention-check failures**
- `( )` → number of **false alarms**, i.e., trials in which:
  - the trial was a normal trial (keys 1, 2, or 3 expected), but  
  - the participant responded with the attention-check key (`G`)
- `{ }` → number of **easy-trial failures** (present only in Single Duration blocks)

*Easy trials* are defined as trials in which the difference between standard and deviant durations is large (e.g., 1.4 vs. 4).  
These annotated values were used during preprocessing to identify and exclude low-quality participants from further analyses.

- **Columns 9–14: Mean block performance (cleaned)**  
These columns contain only the mean performance values for each block and participant, without additional annotations.

- **Columns 15–26: Transposed-interval difference metrics**  
These columns report the mean difference between transposed intervals for **correctly** and **incorrectly** answered trials in each block.

In each sequence trial of the experiment:
- Three stimuli were presented
- One stimulus was deviant, created by **transposing two intervals** in the sequence

Example:
- Standard stimulus: `22314`
- Deviant stimulus: `22134`  
  (intervals `1` and `3` are transposed)

In Single Duration trials, these values instead reflect the difference between standard and deviant durations.

These measures were derived to test the hypothesis that performance in beat (Reg) and non-beat (Irreg) blocks varies as a function of the magnitude of interval transposition—specifically, that larger differences facilitate discrimination.

For example:
- `AudRegIntDiff (T)` represents the average transposed-interval difference for **correct trials** in the auditory beat (regular) block.

- **Columns 28–33: Block presentation order**  
These columns indicate the order in which each block was presented to each participant.  
Block order was randomized across participants.

These data were later used to assess potential order effects, such as whether completing auditory blocks earlier improved performance in subsequent visual blocks.

---

## PreprocessedResults_101participants.csv

- **Description:**  
  This spreadsheet is the preprocessed version of `PrimaryResults_132participants.xlsx`.

- **Participant exclusion criteria:**  
  After compiling results from all 132 participants, individuals were excluded from subsequent analyses if they met **any** of the following criteria:
  - Performance at chance level (33%) in **four or more blocks**
  - More than five Failure to correctly identify attention-check trials or false alarms.

  As a result, data from **31 participants** were excluded, yielding a final sample size of **N = 101**.

- **Additional variables:**  
  A column representing **years of musical instruction** was added from `end_of_study_Q.xlsx` to this dataset:
  - `1` → less than 5 years of musical instruction  
  - `2` → 5 or more years of musical instruction  

  This variable was required for subsequent statistical analyses and visualizations.

- **Column removal:**  
  Columns 2–7 from `PrimaryResults_132participants.xlsx` (block-wise performance with detailed annotations) were removed in this file, as they were not required for downstream analyses.

---

## Three_Auditory_clusters.csv  
## Three_Auditory_clusters_2.csv

- **Description:**  
  These files contain the results of a clustering analysis performed on the auditory modality data.

- **Analysis rationale:**  
  A Silhouette analysis indicated that **three clusters** provided the optimal clustering solution for auditory performance. Based on this result, participants were assigned to three clusters using a k-means clustering approach.

- **Input:**  
  `PreprocessedResults_101participants.csv`

- **Analysis code:**  
  `clustering analysis/K-means/Online_auditory_kmeans.ipynb`

- **Outputs:**  
  - `Three_Auditory_clusters.csv`  
  - `Three_Auditory_clusters_2.csv`

- **Purpose:**  
  These datasets were generated for visualization purposes:
  - `Three_Auditory_clusters.csv` is used for **scatter plot** visualizations  
  - `Three_Auditory_clusters_2.csv` is used for **bar plot** visualizations  

  The final plots produced from these files are stored in the `plots/` folder.

- **Notes:**  
  - Column labels indicate cluster membership:
    - `0` → Cluster 1  
    - `1` → Cluster 2  
    - `2` → Cluster 3

---

## Two_Visual_clusters.csv  
## Two_Visual_clusters_2.csv

- **Description:**  
  These files contain the results of a clustering analysis performed on the visual modality data.

- **Analysis rationale:**  
  A Silhouette analysis indicated that **two clusters** provided the optimal clustering solution for visual performance. Based on this result, participants were assigned to two clusters using a k-means clustering approach.

- **Input:**  
  `PreprocessedResults_101participants.csv`

- **Analysis code:**  
  `clustering analysis/K-means/Online_visual_kmeans.ipynb`

- **Outputs:**  
  - `Two_Visual_clusters.csv`  
  - `Two_Visual_clusters_2.csv`

- **Purpose:**  
  These datasets were generated for visualization purposes:
  - `Two_Visual_clusters.csv` is used for **scatter plot** visualizations  
  - `Two_Visual_clusters_2.csv` is used for **bar plot** visualizations  

  The final plots produced from these files are stored in the `plots/` folder.

- **Notes:**  
  - Column labels indicate cluster membership:
    - `0` → Cluster 1  
    - `1` → Cluster 2  
