# testing reading a csv
# author Andrew Beatty

import csv

filename = "test.csv"

with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    firstLine = True
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        print (line[2])


email = "qwerty@QWERT.ie"
print (email.find('@'))
start = email.find('@')
print (email[start+1:])