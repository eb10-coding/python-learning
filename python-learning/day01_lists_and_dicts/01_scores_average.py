# variables
scores = [55, 72, 90, 43, 61, 88]
num_of_scores = 0
total_score = 0
num_of_fail = 0
num_of_scores = len(scores)
# calcuting mean
for i in range(len(scores)):
    total_score += scores[i]

mean = total_score / num_of_scores
print("the average score is", mean)
# how many fail

for i in range(len(scores)):
    if scores[i] < 60:
       num_of_fail += 1
print(num_of_fail, "have failed")
