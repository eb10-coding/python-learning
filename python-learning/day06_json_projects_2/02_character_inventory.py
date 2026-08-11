# chracter inventory system
import os
import json

target_dir = "player_data"
filename = "inventory.json"
file_path = os.path.join(target_dir,filename)
os.makedirs(target_dir,exist_ok=True)
data = {}

try:
    with open(file_path) as file:
        data = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    data = {}

mode = input("choose mode ('view', 'add', 'use','clear'): ")
if mode == "add":
    while True:
        item_name = input("enter item name: ")
        if item_name == "done":
            break
        item_type = input("enter item type: ") # operation location/indenation may need to be changed
        while True:
            try:
                item_quant = int(input("enter quantity: "))
                if item_name.lower() in data:
                    data[item_name.lower()]["quantity"] += item_quant
                else:
                    data[item_name.lower()] = {"quantity": item_quant,"type":item_type}
                break
            except ValueError:
                print("this is not a valid integer, retry ")
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)
elif mode == "view":
    if not data:
        print("empty inventory")
    else:
        for item_name, details in data.items():
            print(f"Item: {item_name} | Qty: {details['quantity']} | Type: {details['type']}")
elif mode == "use":
    item_check = input("enter item name to use: ")
    if item_check in data:
        data[item_check]["quantity"] -= 1
        print(f"you have used 1 {item_check}")
        with open(file_path,"w") as file:
                    json.dump(data,file,indent=4)
        if data[item_check]["quantity"] <= 0:
            del data[item_check]
            
            
    else:
        print("you dont have this item ")

elif mode == "clear":
    data = {}
    with open(file_path,"w") as file:
        json.dump(data,file,indent=4)