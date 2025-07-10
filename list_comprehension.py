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
for i in range(x):
      for j in range(y):
            for k in range(z):
                  if i + j + k != n:
                        print(i,j,k)
                        
                 


