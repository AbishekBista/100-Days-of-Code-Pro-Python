# get the total bill amount
total_bill_amount = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give(10, 12, or 15)? "))
number_of_people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill_amount + total_bill_amount * tip_percentage / 100

each_person_owes = round(bill_with_tip / number_of_people, 2)

print(f"Each person should pay: ${each_person_owes}")