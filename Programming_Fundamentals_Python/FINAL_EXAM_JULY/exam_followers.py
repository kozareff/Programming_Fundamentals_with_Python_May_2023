followers = {}

while True:
    actions = input()
    if actions == 'Log out':
        break

    counter = actions.split(': ')
    commands = counter[0]
    username = counter[1]

    if commands == 'New follower':
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}

    elif commands == 'Like':
        likes_number = int(counter[2])
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
        followers[username]['likes'] += likes_number

    elif commands == 'Comment':
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
        followers[username]['comments'] += 1

    elif commands == 'Blocked':
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f'{len(followers)} followers')

for name, counter in followers.items():
    total = counter['likes'] + counter['comments']
    print(f'{name}: {total}')