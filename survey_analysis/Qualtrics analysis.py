
from pathlib import Path
import pandas as pd
## 81: Complete
## 80: Unique ID
## Years of Ins = 63,65,67,69,71
## Years of Playing = 64,66,68,70,72
participants = []
def isNaN(num): #Checks if Variable has something in it
    return num != num
def getInt(str): #Gets numbers from a string, Example: From "3 yeas" Returns 3.
   s = ''.join(x for x in str if x.isdigit())
   if(s == ""):
      return 0
   return int(s)
ex = pd.read_excel('../data/End_of_study_questionnaire_101.xlsx')
for index,row in ex.iterrows():
   if(index == 0):   # I don't get this part! It should normally iterrate over indexes so we get participants one by one!
      continue
   if(int(row[81]) == 1): # row "complete" it shows if participants have completed the experiment or not
      uniqueId = row[80] # UniqueID
      age = row[43]
      gender = row[44]
      yearsOfPlaying = 0
      yearsOfIns = 0
      YOI = [63,65,67,69,71]
      YOP = [64,66,68,70,72]
      for I in YOP:
         if(isNaN(row[I]) == False):
            yearsOfPlaying += getInt(row[I])
      for I in YOI:
         if(isNaN(row[I]) == False):
            yearsOfIns += getInt(row[I])
      LRHand = 1 if int(row[46]) == 1 else 2 # it refers to a column in file called "which hand do you write with?" and answer would be either 1 or 2

      if yearsOfIns >= 5:
         YOI = 2
      else:
         YOI = 1
      if yearsOfPlaying >= 5:
         YOP = 2
      else:
         YOP = 1
      tmp = {          # here we create a dictionary. One dictionary per person!
         'Unique id': getInt(uniqueId),
         'Age': pd.to_numeric(age), # we use pd.to_numeric to convert strings to numbers. Notice that if there are NaN cells it doesn't give error and just returns NaN
         'Gender [1:F, 2:M]': gender,
         'Musician_years of playing ( >= 5 -> 2 )': YOP,
         'Musician_years of instruction ( >= 5 -> 2 )': YOI,
         'years of instruction': yearsOfIns,
         'years of playing': yearsOfPlaying,
         'L/R Hand [1:R, 2:L]': LRHand
      }
      participants.append(tmp) # append dictionaries to the list 'participants'. So we will have a list filled with dictionaries!
print(participants)
print(type(age))

df = pd.DataFrame(participants) # converts the list into data frame
writer = pd.ExcelWriter('../results/end_of_study_Q.xlsx', engine='xlsxwriter') # creates an excel file
df.to_excel(writer, sheet_name='sheet1', index=False)  # puts the dataframe into the excel file
writer.save()
print(df.groupby('L/R Hand [1:R, 2:L]').size())
print(df.groupby('Gender [1:F, 2:M]').size())
a=df['Age'].mean()
print(f'average of age is {a}')
print(df.groupby('Musician_years of instruction ( >= 5 -> 2 )').size())
print(df.groupby('Musician_years of playing ( >= 5 -> 2 )').size())

