

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

num1 = int(input("Enter the first number: "))

for operation in operations:
    print(operation)

operation = input("Choose an operation: ")

num2 = int(input("Enter the second number: "))

function = operations[operation]
result = function(num1, num2)

print(f"{num1} {operation} {num2} = {result}")