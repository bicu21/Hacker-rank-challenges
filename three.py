# python arthimetic operation
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print(a + b)
print( a-b)
print(a * b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
#List and tuples 
#List can be changed.
my_list = [1,2,3,4,5]
other_list = [8,4,9,7,2]
# To access element 
print(my_list[3])
# Modify element
my_list[4] = 6
print(my_list)
# Append an element
my_list.append(7)
print(my_list)
# insert element
my_list.insert(1,20)
print(my_list)
# Remove element by value
my_list.remove(20)
print(my_list)
# remove element by index
my_list.pop
print(my_list)
# length of list
print(len(my_list))
# Concatenate list
print(my_list + other_list)
# repeat_list
print(my_list * 2)
# Slice a list 
print(my_list[1:3])

# Tuple Unpacking
x, y, z = (1,2,4)
# Exercice one 
apple = ["apple","banana","chery"]
apple[1] = "orange"
print(apple)


#   Exercise 2
colors = ("red","green","blue")
print(colors[0])
print(colors[2])
print(1,"Avocado")
print(colors)
new_fruits = colors + ("yellow")
print(colors)

# ----------------------------
# 1️⃣ Arithmetic Operations
# ----------------------------
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)          # normal division
print("Floor Division:", x // y)   # division without remainder
print("Modulus:", x % y)           # remainder
print("Exponent:", x ** y)         # x to the power of y

# ----------------------------
# 2️⃣ List Operations
# ----------------------------
numbers = [10, 20, 30, 40, 50]
extra_numbers = [5, 15, 25]

print("\nOriginal list:", numbers)

# Access element
print("Element at index 2:", numbers[2])

# Modify element
numbers[1] = 99
print("After modifying index 1:", numbers)

# Append an element
numbers.append(60)
print("After append:", numbers)

# Insert element at a specific position
numbers.insert(2, 77)
print("After insert at index 2:", numbers)

# Remove element by value
numbers.remove(40)
print("After removing value 40:", numbers)

# Remove element by index
numbers.pop(0)  # removes element at index 0
print("After pop at index 0:", numbers)

# Length of list
print("Length of numbers list:", len(numbers))

# Concatenate two lists
print("Concatenation:", numbers + extra_numbers)

# Repeat a list
print("Repetition:", numbers * 2)

# Slice a list
print("Sliced list (index 1 to 3):", numbers[1:3])

# ----------------------------
# 3️⃣ Tuple Operations
# ----------------------------
person = ("Alice", 25, "Engineer")
print("\nTuple:", person)
print("Name:", person[0])
print("Age:", person[1])

# Tuple unpacking
name, age, job = person
print("Unpacked -> Name:", name, ", Age:", age, ", Job:", job)

# Tuples are immutable, but we can create a new tuple
colors = ("red", "green", "blue")
new_colors = colors + ("yellow",)   # Note the comma for a single item tuple
print("New tuple with extra color:", new_colors)

# ----------------------------
# 4️⃣ String Operations
# ----------------------------
text = "Hello Python!"
print("\nString:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("First 5 characters:", text[:5])
print("Replace 'Python' with 'World':", text.replace("Python", "World"))

