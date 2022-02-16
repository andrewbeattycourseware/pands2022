# more messing with dictionaries
# Here I am looking at for loops
# Author: Andrew Beatty

car = {
    "make": "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags"  : ["pre-owned", "Best Buy", "Dealer"]
}

#print (car)

#for key in car:
#    print (key, ' has value ', car[key])

for key, value in car.items():
    print (key +  ' has a value' , value)