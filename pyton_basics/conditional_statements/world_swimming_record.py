from math import floor

record = float(input())
distance = float(input())
time = float(input())

delay = floor(distance / 15) * 12.5

swim_distance = (distance * time) + delay

difference = abs(record - swim_distance)

if swim_distance < record:
    print(f"Yes, he succeeded! The new world record is {swim_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
