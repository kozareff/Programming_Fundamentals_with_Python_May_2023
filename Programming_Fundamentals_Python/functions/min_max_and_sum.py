numbers_as_string = input().split()
numbers_as_digits = list(map(int, numbers_as_string))

maximum_num = max(numbers_as_digits)
minimum_num = min(numbers_as_digits)
total_sum = sum(numbers_as_digits)

print(f'The minimum number is {minimum_num}')
print(f'The maximum number is {maximum_num}')
print(f'The sum number is: {total_sum}')