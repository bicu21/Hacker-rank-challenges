n = int(input('Enter the number'))
for i in range(n):
    print(i* i)

# git pull origin main --allow-unrelated-histories
# git push -u origin main
# git add .
# git commit -m "Add Day 2 HackerRank solution"
# git push
# Loops
# Loops are used to repeat a block of code multiple times.
#  For loop
# it iterates over a sequence like a list tuple string dictionary.

"""
for variable in sequence:
    # block of code

"""
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruits)
letter = "hello"
for letter in "hello":
    print(letter)
# A while loop repeats as long as a given condition is true.

count = 0
while count < 5:
    print(count)
    count += 1

# Loop control statements
# break = exit the loop immediately.

for i in range(5):
    if i == 3:
        break
    print(i)
for i in range(5):
    if i == 3:
        continue
    print(i)
# Nested loop
# a loop inside another loop.
adj = ["red","big","tasty"]
clothes = ["t-shirt","dress","trouser"]
for a in adj:
    for cloth in fruit:
        print(a,fruit)
        # nesting through indexes

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for fruit in fruits:
        print(a, fruit)

# Exercise
# one 

for i in range(1,11):
    print(i)
    i = i + 1

#  second 
down= 10
while down > 0:
    print(down)
    down = down - 1
    
# third

animals = ["Horse", "Lion", "bee","Ox"]

for animal in animals:
    print(animals)
#   fourth
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
# fifth question
for i in range (0,21):
    if i % 2 != 0:
        continue
    print(i)
# 6th question

for i in range (1,6):
    if i == 5:
        break
    print(i)

string = "python"

for string in "python":
    print("string")











