# Runner up or the second score 
#  Input and output in python
n = int(input("Enter a number"))
scores = list(map(int,input().split())) # reads a list of integers.
# input() used to accept input from the user.
# No matter what we type python always see input function like string. not integers.
# input().split() this will split the numbers we have entered
['2','3','4']  # like this 
#  the int converts the string to the integers but when we have multiple numbers like a list we use map( ) to aply this to all list.

# List in python
# store numbers in List
num = [3,7,6,6,2]
num.sort()
num.sort(reverse=True)
print(num)
highest = max(num)
print(highest)
# set will remove duplicates
unique_number =  set(num)
# The exercise
n = int(input())
arr = map(int, input().split())

unique_scores = list(set(arr))
unique_scores.sort(reverse = True)
runner_up = unique_scores[1]
print(runner_up)









