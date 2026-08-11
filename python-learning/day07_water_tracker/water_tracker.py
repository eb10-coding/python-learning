import os
import json

filename = "water_tracker.json"
data = {}

try:
    with open(filename,"r") as file:
        data = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    data = {}

mode = input("enter mode ('add', 'view', 'goal','clear'): ")
if mode == "add":
    while True:
        date = input("enter the date Year-Month-Day: ")    
        if date == "done":
            break
        else:
            try:
                volume = int(input("enter volume in ml: "))
                if date in data:
                    data[date] += volume
                else:
                    data[date] = volume
            except ValueError:
                print("this is not a valid integer, retry.")
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)
elif mode == "view":
    if not data:
        print("there are no entries ")
    else:
        for date, details in data.items():
            print(f"{date} , {details}ml ")
elif mode == "clear":
    data = {}
    with open(filename,"w") as file:
        json.dump(data,file,indent=0)
elif mode == "goal":
    while True:
        date_check = input("enter todays date: ")
        if date_check in data:
            if data[date_check] >= 2000:
                print("goal met. ")
            else:
                print("goal not yet met. ")
            break
        else:
            print("invalid entry, retry. ")