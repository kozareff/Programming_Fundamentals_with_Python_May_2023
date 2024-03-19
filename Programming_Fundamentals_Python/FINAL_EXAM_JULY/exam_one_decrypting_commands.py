received_string = input()

command = input()

while command != "Finish":
    decrypting_command = command.split(" ")

    if decrypting_command[0] == "Replace":
        current_character = decrypting_command[1]
        new_character = decrypting_command[2]
        received_string = received_string.replace(current_character, new_character)
        print(received_string)

    elif decrypting_command[0] == "Cut":
        start_index = int(decrypting_command[1])
        end_index = int(decrypting_command[2])
        if 0 <= start_index < len(received_string) and 0 <= end_index < len(received_string):
            received_string = received_string[:start_index] + received_string[end_index+1:]
            print(received_string)
        else:
            print("Invalid indices!")

    elif decrypting_command[0] == "Make":
        if decrypting_command[1] == "Upper":
            received_string = received_string.upper()
        else:
            received_string = received_string.lower()
        print(received_string)

    elif decrypting_command[0] == "Check":
        substring = decrypting_command[1]
        if substring in received_string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif decrypting_command[0] == "Sum":
        start_index = int(decrypting_command[1])
        end_index = int(decrypting_command[2])
        if 0 <= start_index < len(received_string) and 0 <= end_index < len(received_string):
            substring = received_string[start_index:end_index+1]
            ascii_sum = 0
            for ascii in substring:
                ascii_sum += ord(ascii)
            print(ascii_sum)
        else:
            print("Invalid indices!")

    command = input()