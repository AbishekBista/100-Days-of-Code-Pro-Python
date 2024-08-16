from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue: 
            symbol = input("Pick an operation: ")
            num2 = float(input("Enter the next number: "))
            function = operations[symbol]
            result = function(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")

            continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start afresh: ")
            if continue_calc == 'y':
                num1 = result
            else:
                should_continue = False
                calculator()
             
calculator()
