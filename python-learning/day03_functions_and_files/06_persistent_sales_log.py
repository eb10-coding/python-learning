# persisten sales log
def format_text(product_name,price):
    return f"{product_name},{price:.2f}\n" #  may need brackets
import os
target_dir = "file"
filename = "sales.txt"
os.makedirs(target_dir,exist_ok=True)
file_path = os.path.join(target_dir,filename)

while True:
    product_name = input("enter product name: ")
    if product_name == "done":
        break
    while True:
        try:
            price = float(input("enter product price: "))
            break
        except ValueError:
            print("this is not a valid number, retry")

    final_line = format_text(product_name,price)
    with open(file_path, "a") as file:
        file.write(final_line)

print("\nSaved Sales Log")
grand_total = 0
with open(file_path,"r") as file:
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        item_price = float(parts[1])
        grand_total += item_price
        print(f"product: {name} | Price: ${item_price:.2f}")

print(f"\nGrand Total: ${grand_total:.2f}")