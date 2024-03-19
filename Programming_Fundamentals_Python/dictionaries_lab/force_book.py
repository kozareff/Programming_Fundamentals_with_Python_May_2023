force_users_group = {}

while True :
    command = input()
    if command == 'Lumpawaroo' :
        break

    if "|" in command :
        force_side, force_user = command.split(" | ")

        if force_side not in force_users_group.keys() :
            force_users_group[force_side] = []
        is_part_of_the_force = False
        for member in force_users_group.values():
            if force_user in member:
                is_part_of_the_force =True
                break

        if not is_part_of_the_force:
            force_users_group[force_side].append(force_user)


        # if force_user not in force_users_group.values() :


    elif "->" in command :
        force_user, force_side = command.split(" -> ")

        for side, member in force_users_group.items() :
            for user in member:
                if force_user == user :
                    force_users_group[side].remove(force_user)
        if force_side not in force_users_group.keys() :
            force_users_group[force_side] = []
        force_users_group[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for force_side, force_user in force_users_group.items():
    if len(force_user) >0 :
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for member in force_user:
            print(f'! {member}')