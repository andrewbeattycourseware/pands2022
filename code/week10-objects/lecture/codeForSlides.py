# this is code I am using the lecture slides
# this is program does not do anything
import datetime

firstname   = 'Andrew'
lastname    =' Beatty'
dob         = datetime.date(2010, 1, 1)
height      = 180
weight      = 100


person1firstname = 'Andrew'
person1lastname = ' Beatty'
person1dob = datetime.date(2010, 1, 1)
person1height = 180
person1weight = 100

person21firstname = 'Joe'
person21lastname = ' bloggs'
person21dob = datetime.date(2010, 2, 2)
person21height = 170
person21weight = 80

firstnames = ['andrew', 'joe', 'mary']
lastnames = ['beatty', 'bloggs', 'meeseeks']
dobs = [
    datetime.date(2010, 1, 1), 
    datetime.date(2010, 2, 2), 
    datetime.date(2013, 3, 3)]
heights = [180, 170, 165]
weights = [100, 80, 55]


def gethealthstats(firstname, lastname, dob, height, weight):
    pass

gethealthstats(firstnames[2], lastnames[2],dobs[2],heights[2],weights[2])

def displayperson(firstname, lastname, dob, height, weight):
    pass

person1 = {
    'firstname'   : 'Andrew',
    'lastname'   : 'Beatty',
    'dob'   : datetime.date(2010, 1, 1),
    'height'   : 180,
    'weight'   : 100
}
person2 = {
    'firstname': 'Joe',
    'lastname': 'Bloggs',
    'dob': datetime.date(2010, 2, 2),
    'height': 170,
    'weight': 80
}
person3 = {
    'firstname': 'Mary',
    'lastname': 'Meeseeks',
    'dob': datetime.date(2015, 3, 3),
    'height': 165,
    'weight': 55
}
persons = [person1, person2, person3]
