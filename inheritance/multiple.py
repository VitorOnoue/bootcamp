class Animal:
    def __init__(self, amount_paws):
        self.amount_paws = amount_paws

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

class Mammal(Animal):
    def __init__(self, color_fur, **kw):
        super().__init__(**kw)
        self.color_fur = color_fur

class Bird(Animal):
    def __init__(self, color_beak, **kw):
        super().__init__(**kw)
        self.color_beak = color_beak
        

class Dog(Mammal):
    pass

class Platypus(Mammal, Bird):
    def __init__(self, color_fur, color_beak, amount_paws):
        super().__init__(color_fur=color_fur, color_beak=color_beak, amount_paws=amount_paws)

dog = Dog(amount_paws=4, color_fur="white-ish")
print(dog)

platypus = Platypus(amount_paws=2, color_beak="yellow-ish", color_fur="green-ish")
print(platypus)