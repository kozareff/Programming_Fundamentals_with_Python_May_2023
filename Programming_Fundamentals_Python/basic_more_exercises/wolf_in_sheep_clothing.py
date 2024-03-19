animals = input()

animal_list = []

start_index = 0
end_index = 1
separated_animals = ''
sheep_num = 0

while True:

    separated_animals = animals[start_index:end_index]

    if 'sheep' in separated_animals:
        animal_list.append('sheep')
        start_index = end_index

    elif 'wolf' in separated_animals:
        animal_list.append('wolf')
        start_index = end_index

    end_index += 1

    if end_index > len(animals) + 1:
        break

animal_list.reverse()

if animal_list[0] == 'wolf':
    print(f'Please go away and stop eating my sheep')

else:
    for sheep_index in animal_list:

        if sheep_index == 'sheep':
            sheep_num += 1

        else:
            break

    print(f'Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!')