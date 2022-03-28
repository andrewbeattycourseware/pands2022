# in this program I look at various ways of reading in data into a dataFrame
# Author: Andrew Beatty

import pandas as pd

# reading in dictionary objects 
# the attribute names will be column names
# the index is automatically made
dataAsDictOfList = {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]
}
df = pd.DataFrame(dataAsDictOfList)
df = pd.DataFrame(dataAsDictOfList, index=['a','b','c'])

#print (df)
#print (df.describe())

# or
dataAsDictOfDict = {
    "Name": {
        '101': "Braund, Mr. Owen Harris",
        '102': "Allen, Mr. William Henry",
        '103': "Bonnell, Miss. Elizabeth",
    },
    "Age": {'101': 22, '102': 35, '104': 58},
    "Sex": {'101': "male", '102': "male", '103': "female"},
}

df = pd.DataFrame(dataAsDictOfDict)
#print (df)

# or with just lists
dataAsLists = [[1, 2, 100, 'male'],
    [2, 4, 100, 'male'], 
    [3, 8, 100, 'female']]

#df = pd.DataFrame(dataAsLists)
df = pd.DataFrame(dataAsLists, columns=['x', 'y', 'percent', 'sex'])

print (df)




