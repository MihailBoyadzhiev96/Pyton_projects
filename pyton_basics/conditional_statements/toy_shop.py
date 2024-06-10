puzzle_price = 2.6
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

price_of_trip = float(input())

number_of_puzzle = int(input())
number_of_dolls = int(input())
number_of_bear = int(input())
number_of_minion = int(input())
number_of_truck = int(input())

amount_of_puzzle = number_of_puzzle * puzzle_price
amount_of_dolls = number_of_dolls * doll_price
amount_of_bear = number_of_bear * bear_price
amount_of_minion = number_of_minion * minion_price
amount_of_truck = number_of_truck * truck_price

total_amount = (amount_of_truck + amount_of_minion + amount_of_bear + amount_of_dolls + amount_of_puzzle)

total_number = (number_of_truck + number_of_minion + number_of_bear + number_of_dolls + number_of_puzzle)

if total_number >= 50:
    total_amount *= 0.75

total_amount = total_amount * 0.9

if total_amount >= price_of_trip:
    print(f"Yes! {total_amount - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_trip - total_amount:.2f} lv needed.")
