# from lab sheet
# 4.	Write a program that stores a student name 
# and a list of her courses and grades in a dict, 
# the program should then print out her data.
# The number of course she has could change.
# in this example the data is hard coded
# Author: Andrew Beatty

student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}

print("Student: {}".format(student["name"]))

# mudules in an array in the dict student
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
