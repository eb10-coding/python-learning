# student grade tracker 2
import os
def text_format(name,score):
    return f"{name},{score:.1f}\n"
target_dir = "school_records"
filename = "grades.txt"
os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)

while True:
    name = input("enter name: ")
    if name == "done":
        break
    while True:
        try:
            score = float(input("enter score: "))
            if 0<= score <= 100:
                break
            else:
                print("score must be between 0-100")
        except ValueError:
            print("this is not a valid number, retry")
    final_line = text_format(name,score)
    with open(file_path,"a") as file:
        file.write(final_line)

total_score = 0
student_count = 0
highest_score = -1
highest_student = ""
# reading file
with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        score = float(parts[1])
        print(f"student:{name}, score:{score:.1f}")
        total_score += score
        student_count += 1
        if score > highest_score:
            highest_score = score
            highest_student = name

print(f"best student is: {highest_student}, with a score of: {highest_score}")
mean = total_score / student_count
print(f"the class average is: {mean}")