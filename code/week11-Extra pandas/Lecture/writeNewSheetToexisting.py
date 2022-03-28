# I came accross an issue of while trying to write a second sheet to 
# an existing workbook.
# this file is me trying to prototype code to do this
# stackoverflow and the issue forum from pands are my sources
# https://github.com/pandas-dev/pandas/issues/3441
# shorter
# https://github.com/pandas-dev/pandas/issues/33264
# Author: Andrew Beatty

import pandas as pd

filename = "testTwoSheet.xlsx"

dataAsDictOfList = {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
}
df1 = pd.DataFrame(dataAsDictOfList)
# this will create or overwrite any the excel book (open in Write mode)
df1.to_excel(filename, sheet_name='number 1', index=False)

# now for the second one
data2 = {
    "Name": [
        "a, b",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
}

df2 = pd.DataFrame(data2)
with  pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
    df2.to_excel(writer, sheet_name="number 2a", index= False)


