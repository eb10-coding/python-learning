import os

target_dir = "beta/2026/saling"
filename = "sales2.txt"


os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)

with open(file_path,"w") as file:
    file.write("geeked\nyour nan's a peadophile\n")

print("done")