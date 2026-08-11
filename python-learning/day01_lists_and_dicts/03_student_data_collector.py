# collecting student data
students = []
while True:
    name = input("enter the students name or 'done' if you are finished entering data  ")
    if name == "done":
        break
    score = int(input("enter the students score "))
    if score < 60:
        passed = "failed"
    else:
        passed = "passed"
    students.append({"name": name, "score": score, "passed": passed})

# student average
num_of_scores = len(students)
total_scores = 0
for i in range(len(students)):
    total_scores += students[i]["score"]

mean = total_scores / num_of_scores
# how many passed or failed

total_passed = 0
total_failed = 0
for i in range(len(students)):
    if students[i]["passed"] == "passed":
        total_passed += 1
    else:
        total_failed += 1

# printing
for i in range(len(students)):
    print(students[i]["name"], "acheived a score of",students[i]["score"],"and has",students[i]["passed"])

print(total_passed,"passed")
print(total_failed,"failed")
print("the class average was:", mean)