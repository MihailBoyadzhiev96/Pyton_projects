year_price = int(input())

basketball_shoes = year_price * 0.6
basketball_shirt = basketball_shoes * 0.8
basketball_ball = basketball_shirt * 0.25
basketball_accessory = basketball_ball * 0.2

all_price_equipment = year_price + basketball_shoes + basketball_shirt + basketball_ball + basketball_accessory

print(all_price_equipment)
