# Messing with dictionaries
# Author: Andrew Beatty

car = {
    "make" : "ford",
    "model" : "modeo",
    "year"  : 2006,
    "owner" : {
        "name" : "andrew",
        "driver-number": 1123
    }
}


print(car["year"])
print(car["owner"]["name"])
print (type(car["owner"].get("names")))
