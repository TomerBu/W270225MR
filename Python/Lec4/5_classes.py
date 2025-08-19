class Car:
    def __init__(self, name, model, weight, color):
        self.name = name
        self.model = model
        self.weight = weight
        self.color = color
    
    def __str__(self):
        return f" Car 🚘: name: {self.name}"
    
    def start(self):
        print(f"{self.name} {self.model} is starting...")


c = Car("Fiat", "uno", 850, "white")
c.start()
print(c)



# def my_print(obj):
#     do_print(obj.__str__())