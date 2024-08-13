import random

# generate a random side
random_side = random.randint(0, 1)

# 0 for Heads and 1 for Tails

if random_side == 0:
    print('Heads')
else:
    print('Tails')