class Animal:
    def __init__(self, name):
        self.name = name

    # str for friendly representation:
    def __str__(self):
        return f"Hey, I'm {self.name}"
    
    # str for debugging - serious representation
    def __repr__(self):
        return f"<Animal name='{self.name}'/>"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print(self.name, 'Woof Woof')

class Cat(Animal):
    def make_sound(self):
        print(self.name, 'Miaoooou')