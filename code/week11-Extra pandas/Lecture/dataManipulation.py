# this module is for functions that I need to 
# do data manipulation
# Author: Andrew Beatty

'''
this gets a series of you unique values from a column that contains 
some of the values in a delimited form
'''
import pandas as pd
import random
import re

def getSeriesOfUnique(dataFrame, nameOfCol, delim = '/'):

    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = dataFrame[nameOfCol].dropna().unique()

    # iterate through it and break up the delimited values
    # I am using a set becaue this will remove duplicates as I add them
    # yes I am sure there is a more efficient way of doing this
    uniqueValues = set([])  # empty set
    for valueInCol in valuesWithDelims:
        #print (staff, ":", type(staff)) # for debugging
        valueAsList = re.split('/', valueInCol)
        uniqueValues.update(valueAsList)
    ds = pd.Series(list(uniqueValues))
    # I take the liberty of sorting this series
    ds.sort_values()
    return ds

'''

I am doing this to demonstrate adding a column
this function is essentially one line
It is only here so I can demonstrate it
''' 
def addColumnAddition(df, newCol ,col1, col2, delim=', '):
    # this could use the cat function or simple additions
    df[newCol] = df[col1] + delim + df[col2] 
    
    # I don't need to return df as it should be changed
    # but i am to allow chaining
    return df

'''
randomise data
based on Column
'''
def randomiseDataOnCol(df, columnName):
    oldSeries = getSeriesOfUnique(df, columnName)
    
    # I haven't checked whish is the quicker randomiser
    # pandas of lists
    oldList = oldSeries.tolist()
    randomiseDataOnList(df, oldList)
    

def randomiseDataOnList(df, oldList):
    newList = oldList.copy()
    random.shuffle(newList)
    #print(oldList) # debug checkig they are different
    #print(newList) # debug
    df.replace(oldList, newList, inplace=True, regex=True)

def clearModuleIds(moduleName):
    # this code is taken from 
    # https://www.geeksforgeeks.org/replace-values-in-pandas-dataframe-using-regex/
    # we could have used replace

    # format XXXXDDDDD (x is letter D is number)
    regex = '^[a-zA-Z]{4}[0-9]{5} '
    if re.search(regex, moduleName):

        # Extract the position of beginning of pattern
        #pos = re.search(regex, moduleName).end()

        # I know the size of what needs to be extracted
        return moduleName[10:]

    else:
        # if clean up needed return the same name
        return moduleName

def randomiseModuleNames(df, columnName):
    oldSeries = getSeriesOfUnique(df, columnName)
    
    # strip out the module codes 
    # i could have done this by finding the list of module ids and replacing them with ''
    cleanedSeries= oldSeries.apply(clearModuleIds)

    #print(cleanedSeries.tolist())  # debug
    randomiseDataOnList(df, cleanedSeries.tolist())

def randomiseStaff(df, df_fakeNames):

    # format the fake names
    # randomise the order
    # from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
    df_fakeNames = df_fakeNames.sample(frac=1).reset_index(drop=True)
    # make the comma seperated name
    addColumnAddition(df_fakeNames, 'fullName', 'last', 'first')
    #print (df_fakeNames) # debug


    ds_staff =getSeriesOfUnique(df, 'Staff (delimited)')
    #print(ds_staff)
    #print(ds_staff.size)  # debug


    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
    # I had a few issues with this, it only liked lists for some reason
    # and it is matching the exact value in the element not subString, regex fixed this
    df.replace(ds_staff.tolist(), df_fakeNames.fullName[:ds_staff.size].tolist(), inplace=True, regex=True)
