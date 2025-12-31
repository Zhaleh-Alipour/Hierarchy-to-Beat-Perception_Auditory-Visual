# Timing Perception Experiment (Auditory & Visual)

## Overview
This repository contains a PsychoPy experiment designed to investigate **human timing perception** and to test the hypothesis that lower-level timing abilities can contribute to beat perception across **auditory** and **visual** modalities. The experiment was developed using **PsychoPy v2021.2.3** and deployed online via **Pavlovia**.

The study consists of **six experimental blocks**, presented in a **randomized order**:
- **3 auditory blocks**
- **3 visual blocks**

Each modality includes the following block types:
1. **Regular (beat-based) patterns**
2. **Irregular (non-beat) patterns**
3. **Single-interval durations**

This repository includes all code, stimuli, and preprocessing scripts required to run the experiment.

---

## Experimental Design

### Trial Structure
- In each trial, participants are presented with **three sequential stimuli**, shown in **random order**.
- **One stimulus differs** from the other two in temporal structure or duration.
- Participants indicate which stimulus was different by pressing **key 1, 2, or 3**.
- Attention check trials require a different response (see below).

---

## Auditory Modality

The auditory modality includes three blocks:
- **Regular (beat-based) patterns**
- **Irregular (non-beat) patterns**
- **Single durations**

### Stimulus Generation
- Auditory stimuli were generated using **MATLAB** script located in the `Matlab/` folder.
- Stimuli were created externally to ensure **high-quality pure tones**, as PsychoPy-generated sounds did not provide sufficient audio fidelity.
- Final audio files were placed into condition-specific folders.
- File paths were referenced via corresponding `.xlsx` files, which were imported into the PsychoPy experiment.

### Audio Folders
- `RegPatterns/` – regular (beat-based) auditory stimuli  
- `IrregPatterns/` – irregular (non-beat) auditory stimuli  
- `SingleDurations/` – single-interval auditory stimuli  

---

## Visual Modality

The visual modality also includes three blocks:
- **Regular (beat-based) patterns**
- **Irregular (non-beat) patterns**
- **Single durations**

### Visual Stimulus Design
- Visual stimuli were created using the **PsychoPy Builder interface**.
- Stimuli consist of a **black square displayed on a gray background**.

#### Beat-Based and Irregular Patterns
- The square alternates between the **left and right sides** of the screen.
- It remains at each location for the **duration of interest**.
- This alternating presentation creates a **rhythmic visual movement**.

#### Single-Interval Condition
- The square appears in the **center of the screen**.
- It remains visible for the **duration of interest**, without lateral movement.

---

## Attention Check Trials

Attention check trials are embedded within **each block** to ensure participant engagement.

### Auditory Attention Checks
- High-pitch tones are used instead of the standard **500-Hz** tones.
- Attention check files are labeled with the word 'pitch' at the end of the filename.
- These stimuli are referenced via separate `.xlsx` files:
  - `pitchReg.xlsx`
  - `pitchIrreg.xlsx`
  - `pitchSD.xlsx`
- Participants must press the **“G” key** instead of keys 1–3.

### Visual Attention Checks
- A **green square** is presented instead of the standard gray square.
- Participants respond using the **“G” key**.

---

## Practice Trials
- Each block begins with **6 practice trials**, two of which are attention checks.
- Practice trials familiarize participants with the task and response mapping.
- Practice trials will not be recorded or analyzed.  

---

## Headphone / Microphone Check
To ensure participants are wearing headphones:
- Participants hear a **spoken three-digit number** before the experiment begins, and must type it correctly to proceed.
- The audio file used for this check is:
  - `four-one-one.mp3`

---

## Volume Calibration
Before the main experiment:
- Participants adjust audio volume to a comfortable level.
- The audio file used for this is:
  - `volset.xlsx`

---

## Visual Size Standardization
To standardize visual stimulus size across devices:
- Participants adjust an on-screen image to match the size of a **physical credit card**.
- This ensures consistent stimulus size regardless of screen dimensions.
- The image used is:
  - `bank-1300155_640.png`

---

## Post-Experiment Questionnaire

After completing the experiment, participants are **automatically redirected** to a questionnaire collecting:
- Demographic information
- Music-related background
- Experiment-related feedback

### Implementation
- The questionnaire was created using **Qualtrics**.
- In **PsychoPy Builder**, the questionnaire links are specified under:
  **Builder View → Settings → Online**.
- The **Completed URL** redirects participants after they finish the experiment.
- The **Incomplete URL** redirects participants if they exit the experiment early.
- Questionnaire link:  
  https://uwo.eu.qualtrics.com/survey-builder/SV_6ofm794x4okN4nY/edit

---

## Online Deployment
- The experiment was developed locally and synchronized to **Pavlovia**.
- Pilot experiment link (not publicly runnable):  
  https://run.pavlovia.org/Zhaleh/phdproject/html

---

## Data Output and Preprocessing
- The experiment outputs a **CSV file**.
- Raw output includes many **extra rows and columns** generated by PsychoPy.
- **Extensive preprocessing is required** before analysis.
- Preprocessing scripts and detailed instructions are provided in:
  - `raw_to_preprocessed/`

---

## Usage

### Requirements
- **PsychoPy v2021.2.3**

### Running the Experiment
1. Open **PsychoPy Builder**.
2. Load the `.psyexp` file.
3. Synchronize the project with Pavlovia.
4. Run the experiment online.

### Local Execution
- To run locally, **all audio files must be in `.wav` format**.

---

## Citation

If you use this experiment, code, or stimuli in your research, please cite the associated preprint:

> Mohammad Alipour, Z., Butler, B., & Grahn, J (2024). *Duration, Sequence, and Beat Perception across Modalities*. Preprint available at: https://osf.io/preprints/psyarxiv/yqbhc_v1

*Note: This manuscript has been submitted to the journal **Multisensory Research** and is currently under its second round of peer review. The citation will be updated upon publication.*

---

## License

This project is released under the **MIT License**.

You are free to use, modify, and redistribute the code and experimental stimuli, provided that appropriate credit is given and the associated work is cited.

---

## Contact

**Zhaleh Mohammad Alipour**  
📧 zhaleh.m.alipour@gmail.com