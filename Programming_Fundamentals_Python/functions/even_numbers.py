numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
# numbers_as_digits = [int(number) for number in numbers-as_string]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


# 5.2

def is_even(number):
    if number % 2 == 0:
        return number


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
# numbers_as_digits = [int(number) for number in numbers-as_string]
result = list(filter(is_even, numbers_as_digits))
print(result)

# 5.3
print([int(number) for number in input().split() if int(number) % 2 == 0])