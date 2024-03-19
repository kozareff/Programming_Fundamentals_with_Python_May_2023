numbers = list(map(float, input().split()))

round_numbers = []

for number in numbers:
    round_numbers.append(round(number))

print(round_numbers)