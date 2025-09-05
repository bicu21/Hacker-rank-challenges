#  List comprehension
squares = [x**2 for x in range(5)]
print(squares)  
# range(start, stop, step)
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,10,2)))
#  Cartesian product 
for x in range(2):
    for y in range(3):
            
            print(x,y)
pairs = [(x, y) for x in range(2) for y in range(3)]

print(pairs)

# Conditional filtering
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  

# Tuple 
# ordered collection of items once it is created we can't change it.
point = (1,2,3)
print(point)
# The exercise
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
z = int(input("Enter the third number:"))
n = int(input("Enter the fourth number"))
for i in range(0, x+1):
      for j in range(0,y+1):
            for k in range(0,z+1):
                  if i + j + k != n:
                        print(i,j,k)

# List comprehension in other day practice
# In Python list is built in data type
"""
Features of list
Oredered items = items have defined order.
mutable = it can be changed added or removed
allow dublicates 
It can contain mixed data types

Accessing element in list .
By index 
example fruits = ["apple","banana", "orange"]
print(fruits([0]) this will give apple.
negative indexing
print([-1]) this will give orange 
Slicing 
example numbe = [1,2,3,4,5,6]
print(number[1:4])
this will give 2,3,4

Common list operations 
 a = []
 a.append(10)
 a.insert(0,5)  0 is index value = 5
 a.extend ([15,20]) values
 a.clear() this will remove all the values.
 
"""
                 





