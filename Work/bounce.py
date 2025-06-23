# bounce.py
#
# Exercise 1.5

height = 100  # meters
num_bounces = 10
loss_factor = 3 / 5

for i in range(1, num_bounces + 1):
    height *= loss_factor
    print(f"{i:>2} {round(height, 4):>6}")
