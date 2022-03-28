# 1. create a simple data frame in python
# 2 describe it
# 3 output to csv file
# 4 out put to excel file
# 5. add a sheet to the excel file
# 6. print a piece of statisical information
# Author Andrew Beatty

import pandas as pd

listDAta= [
    ['John', 'math',        23],
    ['John', 'programming', 66],
    ['Mary', 'math',        45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM',        57],
    ['Mark', 'programming', 70],
    ['Mark', 'math',        73],
    ['John', 'Math', ],
    ['John', 'programming', 61],
    ['John', 'programming', 61],

]

df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))

# writing to files
path = "./data/"
csvFilename = path + 'grades1.csv'
df.to_csv(csvFilename)

excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    # index is true becuase that contains the information about what the numbers are
    df.describe().to_excel(writer, sheet_name="summary")

mean =  df.describe().loc['mean','grade']
print(mean)
# or
mean = df['grade'].mean()
print (mean)
