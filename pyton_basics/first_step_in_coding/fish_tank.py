length_sm = int(input())
width_sm = int(input())
height_sm = int(input())
percent_full = float(input())

volume_sm = length_sm * width_sm * height_sm
total_liters = volume_sm * 0.001 * (1 - percent_full / 100)

print(total_liters)
