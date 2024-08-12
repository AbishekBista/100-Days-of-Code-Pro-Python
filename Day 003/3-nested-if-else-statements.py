height = int(input("Enter your height in cm: "))


if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12 :
        print("Ticket price: $5")
    elif age <=18:
        print("Ticket price: $7")
    else:
        print("Ticket price: $12")
else:
    print("You have to grow taller to go on this ride.")