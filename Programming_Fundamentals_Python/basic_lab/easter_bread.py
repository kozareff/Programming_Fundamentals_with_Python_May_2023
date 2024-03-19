budget = float(input())
price_kilo_flour = float(input())
price_pack_eggs = 0.75 * price_kilo_flour
price_litre_milk = 1.25 * price_kilo_flour

colored_eggs = 0
current_bread_count = 0
price_loaf_of_bread = price_pack_eggs + price_kilo_flour + price_litre_milk / 4

while budget > price_loaf_of_bread:
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs = colored_eggs - (current_bread_count - 2)
    budget = budget - price_loaf_of_bread

print(
    f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")