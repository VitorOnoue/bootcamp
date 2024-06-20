class Vehicle:
    def __init__(self, color, plate, amount_wheels):
        self.color = color
        self.plate = plate
        self.amount_wheels = amount_wheels

    def start_engine(self):
        print("starting engine")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, color, plate, amount_wheels, has_content):
        super().__init__(color, plate, amount_wheels)
        self.has_content = has_content
    
    def is_empty(self):
        print(f"It's {"not " if self.has_content else ""}empty")

mc = Motorcycle("black", "frs-9747", 2)

car = Car("white", "abc-1234", 4)

truck = Truck("purple", "def-5678", 8, True)
truck.is_empty()

print(mc)
print(car)
print(truck)