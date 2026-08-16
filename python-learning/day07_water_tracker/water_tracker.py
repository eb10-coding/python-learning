# imports

import os
import json
import numpy as np
import matplotlib.pyplot as plt


filename = "water_tracker.json"
data = {}

try:
    with open(filename,"r") as file:
        data = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    data = {}

mode = input("enter mode ('add', 'view', 'goal','clear', 'stats', 'chart'): ")
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


elif mode == "stats":
    volume_array = np.array(list(data.values()))
    print(f"mean: {np.round(np.mean(volume_array), 2)}")
    print(f"maximum: {np.max(volume_array)}")
    print(f"minimum: {np.min(volume_array)}")

    
elif mode == "chart":
    dates = list(data.keys())
    volumes = list(data.values())
    plt.bar(dates,volumes)
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.show()