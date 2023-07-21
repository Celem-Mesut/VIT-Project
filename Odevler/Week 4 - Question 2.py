menu = {"kebap" : 15,
        "rice":  10,
        "soup" : 5,
        "friet" : 10,
        "baklava" : 8,
        "kola" : 3,
        "fanta" : 3,
        "ayran" : 2,
        "water" : 1,
        "tea" : 1}

for food,kost in menu.items():
    print(food.capitalize(), "=", kost,"€", sep=" ")

orders = {}

while True:
    order = input("Choose foods (FOR QUIT-> 'q'):").lower()
    if order == "q":
        break
    if order in menu:
        orders[order] = menu[order]
    else:
        print("Choose a food from menu!")

total = 0
for choose, price in orders.items():
    print(choose,"-",price,sep=" ")
    total += price
    
print("Total kost:",total)