# shopping list thing
def apply_discount(price):
    return price * 0.9
item_prices = []
discounted_price =[]
total_price = 0
total_over_ten = 0
while True:
    price = input("what is the price of this item (type 'done' when your list is complete) ")
    if price == "done":
        break
    item_prices.append({"price": int(price)})

for i in range(len(item_prices)):
    discounted = apply_discount(item_prices[i]["price"])
    total_price += discounted 
    discounted_price.append(discounted)
    if int(discounted_price[i]) > 10:
        total_over_ten += 1
    print(discounted_price[i])
    

print("the total cost is:",round(total_price,2))
print("there are",total_over_ten,"items over £10")