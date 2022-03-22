# messing with objects
# Author: Andrew Beatty

class Nameofclass:
    name = ""
    last = ""
    def getfullname(self):
        return self.name + ' ' + self.last
   

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'andrew'
inst2.last = 'beatty'

person = inst
print(person.name)

inst.last = "bloks"
print (person.getfullname())

str1 = "blah de blah"
str2 = str1

str1 += " with bells on top"

print (str2)