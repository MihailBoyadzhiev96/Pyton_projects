number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time = number_of_pages / pages_per_hour
hour_needed = total_time / number_of_days

print(int(hour_needed))