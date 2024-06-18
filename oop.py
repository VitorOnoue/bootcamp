class Bicycle:
    def __init__(self, color, name, year, price):
        self.color = color
        self.name = name
        self.year = year
        self.price = price

    def buzz(self):
        print("(buzzing onomatopeia)")

    def brake(self):
        print(f"braking...\nbraked!")

    def ride(self):
        print("whoosh")

    # def __str__(self):
    #     return f"color: {self.color}\nname: {self.name}\nyear: {self.year}\nprice: {self.price}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"


bike1 = Bicycle("black", "lorem ipsum", 2023, 600)
bike1.brake()
bike1.buzz()
bike1.ride()
print(bike1)