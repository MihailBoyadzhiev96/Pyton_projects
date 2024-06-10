budget = float(input())
staff = int(input())
price_of_wear = float(input())

amount_of_wear = staff * price_of_wear

decor = budget * 0.1

if staff > 150:
    amount_of_wear *= 0.9

total_cost = decor + amount_of_wear

difference = abs(total_cost - budget)

if total_cost > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")

else:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
