import math

num_daily_biscuits = int(input())
num_workers = int(input())
others_biscuits = int(input())

my_biscuits = 0

for x in range(1, 31):
    if x % 3 == 0:
        my_biscuits += math.floor(0.75 * (num_daily_biscuits * num_workers))
    else:
        my_biscuits += math.floor(num_daily_biscuits * num_workers)

difference = ((my_biscuits - others_biscuits) / others_biscuits) * 100

print(f"You have produced {my_biscuits} biscuits for the past month.")
if difference > 0:
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(difference):.2f} percent less biscuits.")