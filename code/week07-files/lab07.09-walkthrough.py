# Program that I wrote during the walk through video
# Author: Andrew Beatty
import json

filename = "storedata.json"


students = []
def displayMenu():
    print("menu")
    print("\t(a) add")
    print("\t(v) view")
    print("\t(s) save")
    print("\t(l) load")
    print("\t(q) quit")
    choice = input("please select (a/v/q):")
    return choice

def getModules():
    modules = []
    modulename = input ("please enter the module name (blank to quit)")
    while (modulename != ""):
        module = {}
        module["name"] = modulename
        module["grade"] = int(input("enter grade"))
        modules.append(module)

        modulename = input("please enter the module name (blank to quit)")

    return modules

def doAdd(students):
    student ={}
    student["name"] = input("please enter name:")
    student["modules"] = getModules()
    students.append(student)
    return students

    
def doView(students):
    for student in students:
        print (student["name"])
        for module in student["modules"]:
            print ("\t", module["name"], "\t:", module["grade"])
    return students

def doSave(students):
    with open(filename, "wt") as f:
        json.dump(students, f)
    print("saved")
    return students

def doLoad(students):
    print("in do load")
    with open (filename, "rt") as f:
        return json.load(f)

menuChoice = {
    'a': doAdd,
    'v': doView,
    's': doSave,
    'l': doLoad
}

choice = displayMenu()
while choice != "q":
    if choice in menuChoice:
        students = menuChoice[choice](students)
    else:
        print ("invalid choice try again")

    choice = displayMenu()

print ("goodbye")
