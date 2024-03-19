lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = lost_fights // 2
total_sword_broken = lost_fights // 3
total_shield_broken = lost_fights // 6
total_armor_broken = total_shield_broken // 2

expenses = total_helmets_broken * helmet_price \
           + sword_price * total_sword_broken \
           + shield_price * total_shield_broken \
           + total_armor_broken * armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
