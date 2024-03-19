items = input().split('|')
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150

for item in items:
    type, price = item.split('->')
    price = float(price)
    price_is_valid = False
    if type == 'Clothes':
        if price <= 50.00:
            price_is_valid = True
    elif type == 'Shoes':
        if price <= 35.00:
            price_is_valid = True
    elif type == 'Accessories':
        if price <= 20.5:
            price_is_valid = True

    if price_is_valid:
        if budget >= price:
            budget -= price
            sell_price = price * 1.4
            profit += sell_price - price
            sell_prices.append(sell_price)

for sell_price in sell_prices:
    print(f'{sell_price:.2f}', end = ' ')
print()

print(f'Profit: {profit:.2f}')
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')