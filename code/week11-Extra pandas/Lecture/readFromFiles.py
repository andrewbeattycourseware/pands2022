# demonstrate reading from TSV and excel
# Author Andrew Beatty

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = 'originalData.tsv'
workbookFileName = 'timetableData.xlsx'
df = pd.read_table(filename)

df.to_excel(workbookFileName, sheet_name='activities', index=False)


ds_staff = dataManipulation.getSeriesOfUnique(df, 'Staff (delimited)')

#print (ds_staff) # debug I should use logging
# we have to use a different engin (openpyxl) to append to the book
with pd.ExcelWriter(workbookFileName, engine='openpyxl', mode='a') as writer:
    ds_staff.to_excel(writer, sheet_name="staff", index=False)






