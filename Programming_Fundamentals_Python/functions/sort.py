numbers_string = list(input().split())
numbers_digits = list(int(x) for x in numbers_string if type(x) == str)

print(sorted(numbers_digits))