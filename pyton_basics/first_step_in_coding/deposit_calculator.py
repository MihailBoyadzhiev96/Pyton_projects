deposit_sym = int(input())
deposit_term = int(input())
year_percent = float(input())

per_month = ((deposit_sym * year_percent/100)/12)
total_sum = ((deposit_sym) + deposit_term * per_month)

print(total_sum)