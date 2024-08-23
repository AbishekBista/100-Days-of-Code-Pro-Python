def calculate(n, **kwargs):
    print(kwargs) # dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

# Class with kwargs

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
    
my_car = Car(make="Nissan")
print(my_car.model)