# Nested List
students = [
   ['Alice', 45],
   ['Lydia', 67],
   ['Bicu', 95]
    

]
name, score = students
scores = [scores for name, socore in students]
print(scores)
# What is list of scores only