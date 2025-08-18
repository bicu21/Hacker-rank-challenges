# Python division
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print(a // b)
print(a / b)

# Dictionary and set 
# Stores value as key and value pair.
my_dict = {
    "name" :"Lydia",
    "age" : 21,
    "city": "Ejere"
}
# Dictionary operations
# Access value
print(my_dict["name"])
# Adding other key and value pair 
my_dict["country"] = "kenya"
print(my_dict)
# Modify value
my_dict["age"] = 26
print(my_dict)
# Remove pair by key
del my_dict["city"]
print(my_dict)
# Safe get value
my_dict.get("age")
print(my_dict)
# Check existance 
"name" in my_dict
print(my_dict)
#  length of the dictionary
print(len(my_dict))
# Clear all
# my_dict.clear()


# Set
# Set is unordered collection of items this means every item appears only once.
my_set = {1,2,3,4}
print(my_set)
print(my_set.add(5))
print(my_set.remove(3))
print(5 in my_set)
len(my_set)
# union 
a =  {1,2,3,4,5}
b = {9,8,7,6,5,4}
print(a | b)
# Intersection
print( a & b)
# difference
print(a -b)
