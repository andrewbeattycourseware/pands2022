import json
filename="testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict 
    # we can do this later
    with open(filename) as f:
        return json.load(f)

# test the function
somedict = readDict()
print(somedict)