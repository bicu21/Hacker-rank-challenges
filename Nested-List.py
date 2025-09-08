# Nested List
student = [
   ['Alice', 45],
   ['Lydia', 67],
   ['Bicu', 95]
    

]
# name, score = students
# scores = [scores for name, socore in students]
# print(scores)
# What is list of scores only
# Next day
# Sorting in python
# Two methos of sorting
num = [5,6,7,2,1,4,9,4]
num.sort()
print(num)
# using sorted 
sorted_numbers = sorted(num)
print(num)
name = ["zed", "lydia", "chala"]
sorted_names = sorted(name, key=str.lower)
print(name)
#  Exercise 
numbers = [12, 4, 56, 17, 8, 99, 23]
sorted_numbers = sorted(numbers)
print(numbers)
names = ["Zara", "Liam", "Emma", "Noah", "Olivia"]
sorted_names = sorted(names)
print(names)

students = [["John", 75], ["Jane", 82], ["Dave", 75], ["Dana", 90]]
# Sorting the list by name and alphabetically
students.sort(key=lambda x: (x[1], x[0]))
print(students)
# Input: Number of students
n = int(input())

students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Extract all grades and find the unique sorted grades
grades = sorted(set([student[1] for student in students]))

# The second lowest grade
second_lowest = grades[1]

# Filter names having the second lowest grade
result = [student[0] for student in students if student[1] == second_lowest]
result.sort()

# Print names alphabetically
for name in result:
    print(name)
# Simple nested list with equal-length inner lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested list with varying lengths of inner lists
nested_list_varied = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

# Nested list with mixed data types
nested_list_mixed = [["Alice", 30], ["Bob", 25], ["Charlie", 35]]
# Creating a nested list with different types of elements
nested_list = ["Python", 35, [1, 3, 5, 7]]

# Access elements of nested list
print("First element:", nested_list[0])  # Python
print("Second element:", nested_list[1]) # 35
print("Third element (list):", nested_list[2]) # [1, 3, 5, 7]

# Access elements inside the sub-list
print("First element of sub-list:", nested_list[2][0]) # 1
print("Second element of sub-list:", nested_list[2][1]) # 3
print("Third element of sub-list:", nested_list[2][2]) # 5
print("Fourth element of sub-list:", nested_list[2][3]) # 7
# Creating a list (works like an array)
arr = [10, 20, 30, 40]

# Access elements
print(arr[0])   # 10
print(arr[-1])  # 40 (last element)

# Modify elements
arr[1] = 25
print(arr)  # [10, 25, 30, 40]

# Add elements
arr.append(50)
print(arr)  # [10, 25, 30, 40, 50]

# Remove elements
arr.remove(30)  # removes first occurrence
print(arr)  # [10, 25, 40, 50]

# Iterate
for num in arr:
    print(num)

