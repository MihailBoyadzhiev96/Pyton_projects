price_nylon = 1.5
price_color = 14.50
water_price = 5
bag_price = 0.4

number_nylon = int(input())
color_litters = int(input())
water_quantity = int(input())
hours_of_work = int(input())

sum_of_materials = ((number_nylon + 2) * price_nylon) + ((color_litters * 1.1) * price_color) + \
                   ((water_quantity * water_price) + bag_price)
work_amount = (sum_of_materials * 0.3) * hours_of_work

total_sum = sum_of_materials + work_amount

print(total_sum)
