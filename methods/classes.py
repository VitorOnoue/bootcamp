class Person:
    def __init__(self, name=None, age=None):
        self._name = name
        self._age = age

    @classmethod
    def create_by_birthdate(cls, y, m, dd, name): # cls is convention
        # no logic for month and day
        age = 2024 - y
        return cls(name, age)
    
    @staticmethod
    def age_majority(age):
        return age >= 18
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

person = Person.create_by_birthdate(2004, 3, 2, "vkko") # calling method without instances
print(person.name, person.age)
print(person.age_majority(person.age))