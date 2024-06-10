# Четене на входните данни
budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

# Изчисляване на цените на всеки от продуктите
video_card_price = 250 * video_cards
processor_price = 0.35 * video_card_price * processors
ram_price = 0.1 * video_card_price * ram_memory

# Изчисляване на общата сума без отстъпката
total_price = video_card_price + processor_price + ram_price

# Проверка за отстъпка
if video_cards > processors:
    total_price *= 0.85

# Проверка дали бюджета е достатъчен
if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
