# Четене на входните данни
product = input()

# Проверка дали продуктът е плод
if product == "banana" or product == "apple" \
        or product == "kiwi" or product == "cherry" \
        or product == "lemon" or product == "grapes":
    print("fruit")
# Проверка дали продуктът е зеленчук
elif product == "tomato" or product == "cucumber" \
        or product == "pepper" or product == "carrot":
    print("vegetable")
# Ако не е плод или зеленчук, считаме го за "unknown"
else:
    print("unknown")
