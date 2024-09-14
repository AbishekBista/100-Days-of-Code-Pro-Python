def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Function can be passed to other functions

def calculate(passed_function, n1, n2):
    result = passed_function(n1, n2)
    print(result)

calculate(multiply, 1, 2)

# Function can be nested

def outer():
    print("I'm outer")
    
    def inner():
        print("I'm inner")
    
    inner()

outer()
#inner() Cannot invoke inner function from outside of the scope

# Inner function can be returned to be invoked later

def box():
    print("I'm a box")

    def chocolate():
        print("I'm chocolate")
    
    return chocolate

chocolate_function = box()
chocolate_function()