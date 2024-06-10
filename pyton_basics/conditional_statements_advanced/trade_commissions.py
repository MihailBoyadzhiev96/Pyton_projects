# Четене на входните данни
city = input()
sales_volume = float(input())

# Проверка за валидност на обема на продажбите
if sales_volume < 0:
    print("error")
    exit()

# Изчисляване на търговската комисионна според града и обема на продажбите
if city == "Sofia":
    if sales_volume <= 500:
        commission = 0.05
    elif 500 < sales_volume <= 1000:
        commission = 0.07
    elif 1000 < sales_volume <= 10000:
        commission = 0.08
    else:
        commission = 0.12
elif city == "Varna":
    if sales_volume <= 500:
        commission = 0.045
    elif 500 < sales_volume <= 1000:
        commission = 0.075
    elif 1000 < sales_volume <= 10000:
        commission = 0.10
    else:
        commission = 0.13
elif city == "Plovdiv":
    if sales_volume <= 500:
        commission = 0.055
    elif 500 < sales_volume <= 1000:
        commission = 0.08
    elif 1000 < sales_volume <= 10000:
        commission = 0.12
    else:
        commission = 0.145
else:
    print("error")
    exit()

# Изчисляване на търговската комисионна
commission_amount = commission * sales_volume

# Отпечатване на резултата
print(f"{commission_amount:.2f}")
