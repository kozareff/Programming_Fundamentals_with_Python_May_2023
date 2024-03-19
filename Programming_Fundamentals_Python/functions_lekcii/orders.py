def price_calculation(order, quantity) :

    if order == 'coffee' :
        print(f'{quantity * 1.5:.2f}')
    elif order == 'water' :
        print(f'{quantity * 1.0:.2f}')
    elif order == 'coke' :
        print(f'{quantity * 1.4:.2f}')
    elif order == 'snacks' :
        print(f'{quantity * 2.0:.2f}')


order = input()
quantity = int(input())

price_calculation(order, quantity)