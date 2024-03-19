numbers = list(map(int, input().split()))
command = input()

while command != "Finish":
    command = command.split()
    command_action = command[0]
    command_value = int(command[1])

    if command_action == "Add":
        numbers.append(command_value)
    elif command_action == "Remove":
        numbers.remove(command_value)
    elif command_action == "Replace":
        replacement = int(command[2])
        if command_value in numbers:
            numbers[numbers.index(command_value)] = replacement
    elif command_action == "Collapse":
        numbers = [values for values in numbers if values >= command_value]
    command = input()

print(*numbers)