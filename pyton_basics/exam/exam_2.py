days = int(input())
room_type = input()
review = input()

price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
elif room_type == "president apartment":
    price_per_night = 35

total_price = days * price_per_night

if days > 15:
    if room_type == "apartment":
        total_price *= 0.50
    elif room_type == "president apartment":
        total_price *= 0.80
elif 10 <= days <= 15:
    if room_type == "apartment":
        total_price *= 0.65
    elif room_type == "president apartment":
        total_price *= 0.85
elif days < 10:
    if room_type == "apartment":
        total_price *= 0.70
    elif room_type == "president apartment":
        total_price *= 0.90

if review == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

total_price = round(total_price, 2)

print(f"{total_price:.2f}")
