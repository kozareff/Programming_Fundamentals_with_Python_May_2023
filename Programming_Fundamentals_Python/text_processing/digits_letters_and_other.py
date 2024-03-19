text = input()

numbers, characters, others = [], [], []

for char in text :
    if char.isnumeric() :
        numbers.append(char)
    elif char.isalpha() :
        characters.append(char)
    else :
        others.append(char)

print(''.join(numbers))
print(''.join(characters))
print(''.join(others))