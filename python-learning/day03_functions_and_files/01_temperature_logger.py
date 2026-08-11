# temperature logger    
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
list = []
while True:
    location = input("Location: ")
    if str(location) == "done":
        break
    temperature = int(input("Temperature in C: "))
    list.append({"location": location,"temperature":temperature})

for i in range(len(list)):
    list[i]["farenheit"] = celsius_to_fahrenheit(list[i]["temperature"])

# average celsius temp
c_total = 0
number_of_temps = len(list)
for i in range(len(list)):
    c_total += list[i]["temperature"]
celsius_average = round(c_total / number_of_temps,2)
# how many below freezing
below_freezing = 0
for i in range(len(list)):
    if list[i]["temperature"] <= 0:
        below_freezing += 1

for i in range(len(list)):
    print(list[i]["location"],":",list[i]["temperature"],"C ",list[i]["farenheit"],"f")

print("the average temperature in celsius is: ",celsius_average)
print(below_freezing,"are below 0")
