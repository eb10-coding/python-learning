# the movie w(atchlist

import os
import json

target_dir = "media_tracker"
filename = "movies.json"
os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)
media = []
mode = input("do you want to 'view', 'add' or 'reset' your watchlist? ").strip().lower()
try:
    with open(file_path,"r") as file:
            media = json.load(file)
except FileNotFoundError:
    media = []


if mode == "view":
    try:
        with open(file_path,"r") as file:
            media = json.load(file)
            print(media)
    except(ValueError, json.JSONDecodeError):
        print("this file is not created or corrupted sorry")
elif mode == "add":
    while True:
        title = input("enter the film title: ")
        if title == "done":
            break
        while True:
            try:
                rating = float(input("Enter the rating x/10: "))
                if 0 <= rating <= 10:
                    break
                else:
                    print("must be between 0 and 10 ")
            except ValueError:
                print("this is not a valid number retry,")

        media.append({"title":title, "rating": rating})

with open(file_path,"w") as file:
    json.dump(media,file,indent=4)

if mode == "reset":
    media = []
    with open(file_path,"w") as file:
        json.dump(media,file,indent=4)