#Python-if-else
n = int(input("Enter number").strip())
if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not weird')
elif n % 2 == 0  and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not weird')


 number = 9
if number == 0:
    print("This number is Zero.")
elif number > 0:
    print("This is number is positive number.")
else:
    print("This number is negative number.")

#  If condition is the condition that evaluate either true or False.
# Python data types 
"""
String = "Hello" anything in the quote.
integer = whole numbers .
boolean = have True , False values.
float = decimal numbers.
List = oredered collections [1]
Lists are mutable oredered collections meaning we can change add or modify value and we can store any data type here.
my_list = [1,3,"Lydia"]

tuple = immutable oredered collections meaning we can't change anything. faster and more efficent  because they cannot changed (23, 'Lydia')
my_tuple = 
dictionary = key-value pairs example {"name" : "Lydia",
'age' : 21,

}
set = collection of unique items = like  fruits = {"apples", "Orange"}
converting data types 
to string = str(x)
to integer = int(y)
float(z)
"""
#  Exercise one 
age = 22
name = "Lydia"
student = True

print("my age is ", age)
print("My name is", name)
print("Is she a student", student)

# Exercise two

length = float(input("Enter the length of the rectangle."))
width = float(input("Enter the width of the rectangle"))
Area = length *width
print(Area)
# Exercise 3
Score = float(input("Enter your score"))

if Score >= 90:
    print("Your grade is A.")
elif 80>= Score >= 89:
    print("Your grade is B.")
elif 70 >= Score >= 79:
    print("Your grade is C.")
elif 60 >= Score >= 69:
    print("Your grade is D.")
else:
    print("Your grade is F")

#  the fourth exercise 
W = float(input("Enter your weight."))
H = float(input("Enter your height."))
BMI = W/H**2
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")



