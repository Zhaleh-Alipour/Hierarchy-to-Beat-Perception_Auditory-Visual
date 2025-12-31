
# this code is for getting raw data files that are in the folder called "data", keeping necessary columns, renaming them, and removing
# the rest of columns that are not useful. At the end it saves files in a new folder called "2_preprocessed_data". We need to create this folder ourselves before running the code.
from pathlib import Path
import pandas as pd
# b is the columns of the raw data file we wanna keep. At the left side of : sign is the name of column and on the right side is the name we want to
# assign to it. Each timing level of each modality is written in a separate column.
b={'participant':'participant', 'date':'date', 'expName':'expName', 'SDaud':'AudSD', 'diff-sd':'AudSDdiff', 'main_key_resp_audSD.keys':'AudSDresp',
   'key_resp_16.keys':'AudSDAttentionCh', 'SDdeviantPitch':'SDdeviantPitch', 'IrregAudSequence':'AudIrreg', 'diff-irreg':'AudIrregDiff',
   'main_key_resp_audIrreg.keys':'AudIrregResp', 'key_resp_6.keys':'AudIrregAttentionCh', 'IrregDeviantPitch':'IrregDeviantPitch',
   'RegAudSequence':'AudReg', 'diff-reg':'AudRegDiff', 'main_key_resp_audReg.keys':'AudRegResp', 'keyACaudreg.keys':'AudRegAttentionCh',
   'RegDeviantPitch':'RegDeviantPitch', 'SDinterval':'VisSD','SDspeed':'VisSDspeed', 'SDDiff':'VisSDdiff', 'main_key_resp_visSD.keys':'VisSDresp',
   'SDColor':'VisSDcolor', 'irregNumberOfIntervals':'VisIrreg', 'irregSpeed':'VisIrregspeed', 'irregDiff':'VisIrregDiff',
   'main_key_resp_visIrreg.keys':'VisIrregResp', 'irregColor':'VisIrregColor', 'NumberOfIntervals':'VisReg',
   'Speed':'VisRegSpeed', 'Diff':'VisRegDiff', 'main_key_resp_visReg.keys':'VisRegResp', 'Color':'VisRegColor'}

# the names of raw files look like 10_finalversion_2022_Mar_25_1438.csv. this function gives us the number before underscore _. in this example 10.
# Use it to save the preprocessed results with a shorter name.
def getParticipantNumber(name):
    return name.split('_')[0];

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR/'data'/'1_raw_data'
OUTPUT_DIR = BASE_DIR / "data" / "2_preprocessed_data"

# for csv in Path('data').rglob('*.csv'): If this script and data folder are in the same path we use this code.

for csv in DATA_DIR.rglob('*.csv'):
    print(csv)
    # df = pd.read_csv(f'data/{csv.name}') # it doesnt make sense to save all raw data where we put our code. They should be in folder. this is the way we refer to that folder.
    df = pd.read_csv(csv)
    result = df[['participant', 'date', 'expName', 'SDaud', 'diff-sd', 'main_key_resp_audSD.keys', 'key_resp_16.keys', 'SDdeviantPitch',
                 'IrregAudSequence', 'diff-irreg', 'main_key_resp_audIrreg.keys', 'key_resp_6.keys', 'IrregDeviantPitch', 'RegAudSequence',
                 'diff-reg', 'main_key_resp_audReg.keys', 'keyACaudreg.keys', 'RegDeviantPitch', 'SDinterval', 'SDspeed', 'SDDiff',
                 'main_key_resp_visSD.keys', 'SDColor', 'irregNumberOfIntervals', 'irregSpeed', 'irregDiff', 'main_key_resp_visIrreg.keys',
                 'irregColor', 'NumberOfIntervals', 'Speed', 'Diff', 'main_key_resp_visReg.keys', 'Color']]
    result.rename(columns=b,inplace=True)
    result.to_excel(OUTPUT_DIR/f'Preprocessed{getParticipantNumber(csv.name)}.xlsx',index=None)

