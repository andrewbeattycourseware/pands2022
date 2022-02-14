# more messing with dictionaries
# Here I am looking at for loops
# Author: Andrew Beatty

car = {
    "make": "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags"  : ["pre-owned", "Best Buy", "Dealer"]
}
#print(car)

'''
for key in car:
    print(key, "have a value", car[key])
'''
print (car.items())
for key, value in car.items():
    print(key, "have a value", value)
