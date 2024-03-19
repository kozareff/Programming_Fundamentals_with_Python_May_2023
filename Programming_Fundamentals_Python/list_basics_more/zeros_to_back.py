input_string = input().split(', ')

for i in range(len(input_string)):
    if input_string[i] == '0':
        input_string.remove('0')
        input_string.append('0')

for j in range(len(input_string)):
    input_string[j] = int(input_string[j])


print(input_string)