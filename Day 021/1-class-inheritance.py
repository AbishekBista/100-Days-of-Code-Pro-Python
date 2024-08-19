class Animal:
    def __init__(self):
        self.num_nose_trils = 2
    
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swim")

    def breathe(self):
        super().breathe()
        print("doig this underwater")

fish = Fish()
fish.swim()
fish.breathe()