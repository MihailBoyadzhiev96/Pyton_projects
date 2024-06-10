first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for i in range(2, first_limit + 1, 2):
    for j in range(2, second_limit + 1):
        if j == 2 or j == 3 or j == 5 or j == 7:
            for k in range(2, third_limit + 1, 2):
                print(f"{i} {j} {k}")
