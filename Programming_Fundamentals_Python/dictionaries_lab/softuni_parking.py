number_of_cars = int(input())
registered_cars = {}

for car in range(number_of_cars) :
    current_command = input().split()

    if current_command[0] == 'register' :
        action, user_name, license_plate_number = current_command

        if user_name not in registered_cars:
            registered_cars[user_name]= license_plate_number
            print(f"{user_name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")


    elif current_command[0] == 'unregister' :
        action, user_name = current_command
        if user_name not in registered_cars:
            print(f"ERROR: user {user_name} not found")
        else:
            del registered_cars[user_name]
            print(f"{user_name} unregistered successfully")

for username,license_plate_number in registered_cars.items():
    print(f"{username} => {license_plate_number}")