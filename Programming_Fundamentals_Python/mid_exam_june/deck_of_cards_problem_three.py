def add_card(card):
    if card in list_of_cards:
        print("Card is already in the deck")
    else:
        list_of_cards.append(card)
        print("Card successfully added")

def remove_card(card):
    if card in list_of_cards:
        list_of_cards.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")

def remove_card_index(card_index):
    if card_index >= len(list_of_cards):
        print("Index out of range")
    else:
        del list_of_cards[card_index]
        print("Card successfully removed")

def insert_card(card_index, card_name):
    if card_name in list_of_cards and 0 <= card_index < len(list_of_cards):
        print("Card is already added")
    elif 0 <= card_index < len(list_of_cards):
        list_of_cards.insert(card_index, card_name)
        print("Card successfully added")
    else:
        print("Index out of range")

list_of_cards = input().split(", ")
number_of_commands = int(input())

for card in range(number_of_commands):
    command = input().split(", ")
    command_name = command[0]
    command_card_name = command[1]

    if command_name == "Add":
        add_card(command_card_name)
    elif command_name == "Remove":
        remove_card(command_card_name)
    elif command_name == "Remove At":
        remove_card_index(int(command_card_name))
    elif command_name == "Insert":
        card_name = command[2]
        insert_card(int(command_card_name), card_name)

print(", ".join(list_of_cards))