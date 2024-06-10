import math

# Четене на входните данни
series_name = input()
episode_duration = int(input())
break_duration = int(input())

# Изчисляване на времето за обяд и времето за отдих
lunch_time = break_duration / 8
relax_time = break_duration / 4

# Изчисляване на общото време, нужно за гледане на епизода
total_time_needed = episode_duration + lunch_time + relax_time

# Проверка дали има достатъчно време за гледане на епизода
if total_time_needed <= break_duration:
    free_time = break_duration - total_time_needed
    print(f"You have enough time to watch {series_name} and left with {math.ceil(free_time)} minutes free time.")
else:
    additional_time_needed = total_time_needed - break_duration
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(additional_time_needed)} more minutes.")
