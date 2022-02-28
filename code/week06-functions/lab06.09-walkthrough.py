# Program that I wrote during the walk through video
# Author: Andrew Beatty

students = []
def displayMenu():
    print("menu")
    print("\t(a) add")
    print("\t(v) view")
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

    
def doView(students):
    for student in students:
        print (student["name"])
        for module in student["modules"]:
            print ("\t", module["name"], "\t:", module["grade"])

choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    else:
        print ("invalid choice")


    choice = displayMenu()

print ("goodbye")
