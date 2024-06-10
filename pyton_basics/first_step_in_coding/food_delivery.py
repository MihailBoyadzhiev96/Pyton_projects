chicken_price = 10.35
fish_price = 12.4
vegan_price = 8.15
deliver_price = 2.50

number_of_chicken = int(input())
number_of_fish = int(input())
number_of_vegan = int(input())

sum_menus = (number_of_chicken * chicken_price) + (number_of_fish * fish_price) + (number_of_vegan * vegan_price)
desert_price = sum_menus/5

total_sum = sum_menus + desert_price + deliver_price

print(total_sum)
