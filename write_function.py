# 
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
   
    
    return leap

year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False

    if year % 4 == 0:
        print(True)
    elif year % 100 == 0:
        print(False)
    elif year % 400 == 0:
        print(True)
    
    return leap
year = int(input())
print(is_leap(year))
# Function to greet a user by name
def greet(name):
    return f"Hello, {name}!"

# Function to calculate factorial of a number (recursive)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to sum all elements in a list
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

