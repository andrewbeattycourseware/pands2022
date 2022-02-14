# Messing with dictionaries
# Author: Andrew Beatty

car = {
    "make": "ford",
    "price": 123,
    "owner" : {
        "firstName":"fred",
        "age":12
    }
}



print(type(car))
print (car)

car["model"] = "focus"
print(car)
#make = car["make"]
#notMake = car.get("a;lshdg;lh")
#print (type(notMake))
#print (make)
print(car["owner"]["age"])