# preprocessed_to_xlsx
Scripts for converting preprocessed data files into Excel (.xlsx) format.

## Purpose
This folder contains code for converting preprocessed `.xlsx` files into a spreadsheet file used for general statistical analysis and k-means analysis.


## Files
- `main.js` - Converting Online data

## Input / Output
- **Input:** Preprocessed data files (.xlsx)
- **Output:**: Excel files (`FinalResults.xlsx`) 

## Usage
Bofore running the code install xlsx package:
    - in terminal print `npm install xlsx`
Conversion process involves two functions at the end of the code: 
1. `makeJsonFromXlsx()`
    
    Converts `.xlsx` files from the `result_online` folder into separate JSON files and put them in the `data_online` folder. 
    This function should be run first after commenting out `makeFinalExcelFromJsons()`

2. `makeFinalExcelFromJsons()`
    Converts JSON fils from the `data` folder into a single Excel file (`FinalResults`). 
    This function should be run after commenting out `makeJsonFromXlsx()`

## Notes
- Designed to be run locally
- The `data` folder is located in the same directory as `main.js` 
- The `results` folder is located one level above the `main.js` directory