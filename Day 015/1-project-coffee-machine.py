MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    for key in resources:
        if key == 'milk' or key == 'water':
            print(f"{key.title()}: {resources[key]}ml")
        else:
            print(f"{key.title()}: {resources[key]}g")
    print(f"Money: ${profit}")

def has_enough_resources(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total_amount = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_amount

def add_money(amount):
    return profit + amount
def validate_transaction(choice, total_amount):
    global profit
    actual_cost = MENU[choice]["cost"]
    if total_amount < actual_cost:
        print("Sorry, that's not enough money. Money refunded")
        return -1
    elif total_amount > actual_cost:
        refund_amount = total_amount - actual_cost
        print(f"Here is ${round(refund_amount, 2)} in change")
        
        profit += actual_cost
        return refund_amount
    else:
        
        profit += actual_cost
        return 0

def make_coffee(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

is_machine_off = False

while not is_machine_off:
    option_chosen = input("What would you like? (espresso/latte/cappuccino): ")
    if option_chosen == 'off':
        is_machine_off = True
    elif option_chosen == 'report':
        print_report()
    else:
        has_resources = has_enough_resources(option_chosen)
        if has_resources:
            total_amount = process_coins()
            refund_amount = validate_transaction(option_chosen, total_amount)

            if refund_amount >= 0:
                make_coffee(option_chosen)
                print(f"Here is your {option_chosen}. Enjoy!")