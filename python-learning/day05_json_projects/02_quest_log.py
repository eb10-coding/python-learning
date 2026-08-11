# "gaming quest log" sonion this is geeked
import os
import json

target_dir = "game_data"
filename = "quests.json"
os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)
quest_log = []
try:
    with open(file_path,"r") as file:
        quest_log = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    print("this file does not exist ")
    quest_log = []

mode = input("do you want to do? enter:'view' , 'add', 'complete'  ")

if mode == "add":
    while True:
        name = input("enter quest name: ")
        if name == "done":
            break
        try:
            reward = int(input("how much gold is the reward: "))
        except ValueError:
            print("this is not a valid integer, retry")
        check = input("is the quest completed yes/no: ")
        if check == "yes":
            status = "completed"
        else:
            status = "in progress"
        quest_log.append({"Quest":name, "reward": reward, "Status": status})

        with open(file_path,"w") as file:
            json.dump(quest_log,file,indent=4)

elif mode == "view":
    if quest_log == []:
        print("no active quests")
    else:
        for item in quest_log:
         print(f"Quest: {item['Quest']} | Reward: {item['reward']} | Status: {item['Status']}")
elif mode == "complete":
    quest_check = input("enter the quest name: ").strip()
    found = False
    for item in quest_log:
        if item["Quest"].lower() == quest_check.lower():
            item["status"] = "completed"
            found = True
            print(f"Quest '{item["Quest"]}' is now marked as complete")
            break
    if not found:
        print("quest was not found")
    else:
        with open(file_path,"w") as file:
            json.dump(quest_log,file,indent=4)