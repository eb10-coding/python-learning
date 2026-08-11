# default & keyword arguments in functions

def format_price(amount,discount=0,currency="$"):
    final_amount = amount - discount
    return f"{currency}{final_amount:.2f}"
price = float(input("what is the price: "))
discountQ = input("do you have a discount y/n ")
if discountQ == ["y","Y"]:
    while True:
        try:
            discount = float(input("what is the discount?"))
            break
        except ValueError:
            print("this is not a valid number try again")
else:
    discount = 0

final_price = format_price(price,discount)
print(f"final price: {final_price}")
