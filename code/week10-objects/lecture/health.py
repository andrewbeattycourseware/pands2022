# use person module
# Author: Andrew Beatty

from personmodule import *
import datetime as dt

person1 = {
    'firstname': 'andrew',
    'lastname': 'beatty',
    'dob': dt.date(2010, 1, 1),
    'height': 180,
    'width': 100
}

# call the functions in the module
# I used import * so these have been imported
# so I can call them with out the module name
displayperson(person1)
gethealthdata(person1)


