# Unlimited Arguments using *

def add(*args):
    return sum(args)

sum = add(1, 2, 3, 4, 5, 6, 7)
print(sum)