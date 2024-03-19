number_of_coffees = 0

while True:
    event = input()
    if event == "END":
        break

    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        number_of_coffees += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        number_of_coffees += 2

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)