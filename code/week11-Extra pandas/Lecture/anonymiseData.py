# this is the script I am using to anonymise the data in the 
# Author: Andrew Beatty

import pandas as pd
import dataManipulation 

filename = 'originalData.tsv'
newFileName = 'anonymisedData.tsv'
fakeNamesFilename ='fakeNames.tsv'

df_fakeNames = pd.read_table(fakeNamesFilename, header=None, names=['first', 'last'])

df = pd.read_table(filename)

dataManipulation.randomiseStaff(df, df_fakeNames)

# now lets randomise the module codes and names
dataManipulation.randomiseDataOnCol(df, "Module ID")

# now randomise module names
dataManipulation.randomiseModuleNames(df, 'Module')

# I am tryiing to have this as similar to the original
# so I am removing the index
df.to_csv(newFileName, index=False, sep='\t')


