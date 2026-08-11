#todo ability to append, rewrite and load json lists

import json
import os

target_dir = "JSON_inventory_manager"
filename = "inventory.json"
os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)
inventory = []
wyd_check = input("enter 'append', 'write: ").strip().lower()
if wyd_check == "append":
    try:
        with open(file_path,"r") as file:
            inventory = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        inventory = []
while True:
    item = input("enter item name: ")
    if item == "done":
        break
    while True:
        try:
            quantity = int(input("enter quantity: "))
            break
        except ValueError:
            print("quantity is not a valid integer, retry")
    inventory.append({"item":item,"qty": quantity})

with open(file_path, "w") as file:
    json.dump(inventory, file,indent=4)

print("inventory saved")