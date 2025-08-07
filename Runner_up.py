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
# Input: list of scores
scores = list(map(int, input("Enter scores separated by space: ").split()))

# Get the highest score
highest = max(scores)

# Remove all occurrences of the highest score
scores = [score for score in scores if score != highest]

# Find the runner-up
runner_up = max(scores)

print("Runner-up score is:", runner_up)
Enter scores separated by space: 2 3 6 6 5
Runner-up score is: 5
def find_runner_up(scores):
    max_score = -float('inf')
    runner_up = -float('inf')
    for score in scores:
        if score > max_score:
            runner_up = max_score
            max_score = score
        elif max_score > score > runner_up:
            runner_up = score
    return runner_up

scores = list(map(int, input().split()))
print(find_runner_up(scores))










