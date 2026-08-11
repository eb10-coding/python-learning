def calculate_ticket_price(base_price,vip_upgrade=False,discount_code=None):
    if vip_upgrade == True:
        base_price += 50
    else:
        base_price += 0
    if discount_code == "SAVE10":
        base_price = float(base_price) * 0.9
    else:
        discount_code = None
    return round(base_price,2)
list =[]
while True:
    name = input("enter name: ")
    if name == "done":
        break
    base_price = float(input("what is the base price of your ticket? "))
    vip_check = input("do you have the vip upgrade? yes/no ")
    vip_upgrade = vip_check == "yes"
    discount_code = input("enter discount code or press 'enter' to skip: ")
    total_price = calculate_ticket_price(base_price,vip_upgrade,discount_code)
    list.append({"name":name,"total":total_price})
revenue = 0
for i in range(len(list)):
    print(f"{list[i]["name"]}, price: ${list[i]["total"]}")
    revenue += list[i]["total"]
print(f"total revenue is ${revenue}")