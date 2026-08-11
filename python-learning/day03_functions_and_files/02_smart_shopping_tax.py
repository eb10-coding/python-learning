# smart shopping list

# collecting the shopping list
list = []
pretax_20 = 0
def calculate_tax(t):
    return t * 1.08
while True:
    item = input("item name: ")
    if item == "done":
        break
    try:
        price = float(input("price: "))
        if price > 20:
            pretax_20 += 1
        taxed_price = round(calculate_tax(price),2)
        list.append({"item":item,"price":price,"taxed":taxed_price})
    except ValueError:
        print("that is not a valid integer.")
final_total = 0
for i in range(len(list)):
    final_total += list[i]["taxed"]
    print(list[i]["item"],": pre tax: ",list[i]["price"],"post tax:",list[i]["taxed"])


print("the total is: ",final_total)
print("there are:",pretax_20,"items above $20")

    