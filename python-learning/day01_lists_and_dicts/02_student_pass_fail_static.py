student = [
    {"name":"alex", "score": 43,"passed": ""},
    {"name":"same", "score": 92,"passed": ""},
    {"name":"Big brother", "score": 13,"passed": ""}
]
for i in range(len(student)):
    if student[i]["score"] < 60:
        student[i]["passed"] = "failed"
    else:
        student[i]["passed"] = "passed"
    print(student[i]["name"],"has", student[i]["passed"])