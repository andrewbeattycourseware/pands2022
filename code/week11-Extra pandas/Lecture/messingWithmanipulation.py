# demonstrate reading from TSV and excel
# Author Andrew Beatty

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = 'originalData.tsv'

df = pd.read_table(filename)
listOfCols = ['Module ID', 'Duration']
print(df[listOfCols].head(2))

df['new'] = df['Duration'] * df['Number of Weeks']

listOfCols = ['Number of Weeks', 'Duration', 'new']
print(df[listOfCols].head(10))
