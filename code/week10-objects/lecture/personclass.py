# person class
# used to demonstrate making an object class

import datetime as dt

class Person:
    def __init__(self, firstname, lastname, dob, height, width):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.height = height
        self.width = width

    def gethealthstats(self):
        print ('health stats for ', self.firstname)
    def display(self):
        print (self)

if __name__ == '__main__':
    person1 = Person('andrew', 'Beatty', dt.date(2010, 1, 1), 180, 100)
    person2 = Person('andrew', 'Beatty', dt.date(2010, 1, 1), 180, 100)
    person3 = Person('andrew', 'Beatty', dt.date(2010, 1, 1), 180, 100)

    people = [person1, person2, person3]

    person1.display()
    person1.gethealthstats()

    # we can add attributes to an instance
    person1.blah = 44
    print (person1.blah)

