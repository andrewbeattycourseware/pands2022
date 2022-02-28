import json
filename="testdict.json"
sample= dict(name='andrew', age=99, grades=[1,34,55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

#test the function
writeDict(sample)