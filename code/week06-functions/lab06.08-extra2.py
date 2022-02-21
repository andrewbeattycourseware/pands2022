# a different way or dealing with the users choice

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice


def doAdd(students):
    print("do add")

def doView(students):
    print("do View")

def doNothing(dumby):
    pass

#the dict that maps a letter to function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # q is a valid choice

}
#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        # run the function
        choiceMap[choice](students)
    else: # use did not enter something valid
        print("\n\nplease select either a,v or q")
    
    choice=displayMenu()
        
        
