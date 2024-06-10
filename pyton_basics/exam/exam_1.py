# Въвеждане на брой хора и разходи
people_count = 20
nights = 14
transport_cards = 30
museum_tickets = 6

# Цени за нощувка, карта за транспорт и билет за музей
price_per_night = 20
price_per_transport_card = 1.60
price_per_museum_ticket = 6

# Изчисляване на общата сума
total_cost_per_person = (nights * price_per_night) + (transport_cards * price_per_transport_card) + (museum_tickets * price_per_museum_ticket)

# Обща сума за цялата група
total_cost = total_cost_per_person * people_count

# Добавяне на 25% за непредвидени разходи
total_cost += total_cost * 0.25

# Отпечатване на общата сума
print(f"{total_cost:.2f}")
