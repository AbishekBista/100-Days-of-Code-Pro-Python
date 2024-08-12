height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))

    if age < 12:
        price = 5
    elif age < 18:
        price = 7
    else:
        price = 12
    
    wantPhotos = input("Do you want photos? (yes / no): ")
    if wantPhotos == "yes":
        price += 3
    
    print(f"Your total bill is {price}")
else:
    print("You cannot ride the rollercoaster")