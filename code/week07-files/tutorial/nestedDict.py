# demo of nested dictionaries
'''
level1= {
    "var" : 34,
    "modules" :[ 
        {
        "name" : "andrew",
        "grade" : 76
    },{
        "name" :"joe",
        "grade" : 44

    }
    ]   
}

def displayAModule(module):
    print (module['name'], '\t', module['grade'] )

def displayModules(modules):
    for module in modules:
        displayAModule(module)


displayModules(level1['modules'])
'''

modules = {
    'course': ['math', 'german'],
    'grades': [23, 66]
}

def displayModules2(modules):
    numberOfModules = len (modules['course'])
    for i in range(0, numberOfModules):
        print (modules['course'][i], '\t', modules['grades'][i])

displayModules2(modules)