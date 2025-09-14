# ----------------------------
# Python Lists & Nested Lists
# ----------------------------

# Simple list
arr = [10, 20, 30, 40]

# Access elements
print("First element:", arr[0])   # 10
print("Last element:", arr[-1])   # 40

# Modify elements
arr[1] = 25
print("Modified list:", arr)  # [10, 25, 30, 40]

# Add elements
arr.append(50)
arr.insert(2, 28)  # insert 28 at index 2
print("After adding elements:", arr)  # [10, 25, 28, 30, 40, 50]

# Remove elements
arr.remove(30)  # removes first occurrence
popped = arr.pop()  # removes last element and returns it
print("After removing elements:", arr)  # [10, 25, 28, 40]
print("Popped element:", popped)  # 50

# Iterate over a list
print("Iterating over list:")
for num in arr:
    print(num)

# List comprehensions
squared = [x**2 for x in arr]
print("Squared values:", squared)

# ----------------------------
# Nested Lists
# ----------------------------
students = [
    ['Alice', 45],
    ['Lydia', 67],
    ['Bicu', 95]
]

# Extract all scores
scores = [score for name, score in students]
print("Scores only:", scores)

# Access elements in nested list
print("First student's name:", students[0][0])
print("First student's score:", students[0][1])

# Nested list with varying lengths & mixed types
nested_list_varied = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
nested_list_mixed = ["Python", 35, [1, 3, 5, 7]]

print("Nested list first element:", nested_list_mixed[0])
print("Nested sub-list element:", nested_list_mixed[2][1])

# ----------------------------
# Sorting Lists
# ----------------------------
num = [5, 6, 7, 2, 1, 4, 9, 4]

# Method 1: sort() - modifies original list
num.sort()
print("Sorted with sort():", num)

# Method 2: sorted() - returns new list
num = [5, 6, 7, 2, 1, 4, 9, 4]
sorted_numbers = sorted(num)
print("Original list after sorted():", num)
print("New sorted list:", sorted_numbers)

# Sorting strings (case-insensitive)
names = ["zed", "Lydia", "chala"]
sorted_names = sorted(names, key=str.lower)
print("Sorted names:", sorted_names)

# Sorting nested lists
students = [["John", 75], ["Jane", 82], ["Dave", 75], ["Dana", 90]]
# Sort by grade, then by name
students.sort(key=lambda x: (x[1], x[0]))
print("Students sorted by grade then name:", students)

# ----------------------------
# User Input and Processing
# ----------------------------
# Find students with second lowest grade
n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    name = input("Enter name: ")
    grade = float(input("Enter grade: "))
    students.append([name, grade])

# Extract grades, find second lowest
grades = sorted(set([student[1] for student in students]))
if len(grades) > 1:
    second_lowest = grades[1]

    # Filter names with second lowest grade
    result = sorted([student[0] for student in students if student[1] == second_lowest])

    print("Students with second lowest grade:")
    for name in result:
        print(name)
else:
    print("Not enough distinct grades to find second lowest.")

# ----------------------------
# Useful List Functions & Tricks
# ----------------------------
example = [3, 6, 1, 9, 2, 6, 3, 8]

print("Length:", len(example))
print("Max:", max(example))
print("Min:", min(example))
print("Sum:", sum(example))
print("Count of 6:", example.count(6))
print("Index of first 6:", example.index(6))

# Reverse a list
example.reverse()
print("Reversed:", example)

# Copy list
example_copy = example.copy()
print("Copy:", example_copy)

# Clear list
example.clear()
print("Cleared list:", example)

# Nested List Iteration
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Iterating nested list:")
for row in matrix:
    for val in row:
        print(val, end=' ')
    print()  # new line after each row

# ----------------------------
# BONUS: Flatten a nested list
# ----------------------------
flattened = [val for row in matrix for val in row]
print("Flattened matrix:", flattened)


