n = int(input("Enter number:"))
for i in range(1,n+1):
    print(i, end="")
# Function in python
# function is a block of re-usable code.
def greet(name):
    # name = parameter.
    print(f"Hello,{name}") # function body

greet("Lydia") # function call
# end represented by n + 1


# exercice one
def arguments(name, age):
    print(f"My name is {name}, and I am {age} years old")
arguments("Lydia", 21)

#  Exercise two
# To make function accept anytype of argument it means the function accept zero or more inputs.
def func1(*args):
    for arg in args:
        print(arg)
    
func1(10,"hello",3.89)

# Exercise three
def calculate(a,b):
    print(a + b)
    print(a -b)
calculate(6,3)

#  Exercise four 
# When we create a function with default argument value if we call the function without providing a value for that argument the function will use the present default value.

def default(name, age, salary= 5000):
    print(f"my name is {name} and I am {age} years old and my salary is {salary}. ")

default("Lydia", 21 )

# Exercise five
# Inner or nested function
def sum(a,b):
    def add(x, y):
        return x + y
    result = add(a,b)
    return result  + 5
print(sum(7,9))

# Exercise six
# Recursive function
# In recursion a function calls itself to solve smaller instances. of the same problem .
def addition(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
addition(10)
    
    

# end represented by n + 1
