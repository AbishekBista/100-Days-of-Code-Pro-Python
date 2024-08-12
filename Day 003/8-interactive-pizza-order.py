print("Welcome to Mario Pizza Deliveries")
pizza_size = input("What size pizza do you want (S/M/L)? ")
add_pepperoni = input("Do you want pepperoni (Y/N)? ")
add_cheese = input("Do you want extra cheese (Y/N)? ")

bill = 0

if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if add_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")