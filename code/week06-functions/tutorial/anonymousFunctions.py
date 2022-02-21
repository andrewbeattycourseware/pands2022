# lambda

def mult(a, b):
    return a * b

def power(a, b):
    return a ** b

#operator = mult
#operator = power
operator = lambda a, b : a + b

print (operator(10, 3))

data = [
    {'name' : "Joe",  'age' : "55"},
    {'name' : "Mary", 'age' :"3"},
    {'name' : "Mark", 'age' : "34"},
    {'name' : "Luke", 'age' : "33"}
]
'''
ages = [33, 55, 12, 1]
sortedAges = sorted(ages)
print(sortedAges)
'''

sortedData = sorted(data, key = lambda x: x['age']) 
for item in sortedData:
    print(item)




