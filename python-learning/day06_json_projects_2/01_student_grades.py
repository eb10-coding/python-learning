import os
import json

target_dir = "classes"
filename = "grades.json"
file_path = os.path.join(target_dir,filename)
os.makedirs(target_dir,exist_ok=True)
students = []
try:
    with open(file_path) as file:
        students = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    students = []
# mode selection
mode = input("choose mode ('view', 'add', 'update'): ")
if mode == "view".lower().strip():
    if not students:
        print("no records in this file")
    else:
        for item in students:
            print(f"Student: {item['name']} | Score: {item['score']} | Passed: {item['status']}")
elif mode == "add":
    while True:
        name = input("enter name: ")
        if name == "done":
            break
        while True:
            try:
                score = int(input("enter score integer: "))
                if 0 <= score <= 100:
                    break
            except ValueError:
                print("not a valid score integer ")
        if score >= 60:
            status = "passed"
        else:
            status = "failed"
        students.append({"name": name, "score": score, "status": status})
        with open(file_path,"w") as file:
            json.dump(students,file,indent=4)
elif mode == "update":
    student_check = input("enter the students name whos score you want to update: ")
    for item in students:
        if item["name"].lower() == student_check.lower():
            new_score = input("enter their new score: ")
            item["score"] = int(new_score)
            if int(new_score) >= 60:
                item["status"] = "passed"
            else:
                item["status"] = "failed"
    with open(file_path,"w") as file:
        json.dump(students, file, indent=4)
elif mode != "view":
    print("list updated ")
else:
    print("")