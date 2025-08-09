class Car:
    number_of_wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(f"{car1.make} {car1.model}")

print(f"Car 1 has {car1.number_of_wheels} wheels.")
print(f"All Car have {car1.number_of_wheels} wheels.")

Car.number_of_wheels = 3
print(f"Now, Car 2 has {car2.number_of_wheels} wheels.")

# class Dog:
#     def bark(self):
#         print("Woof!")

import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """An alternative constructor that uses a birth year."""
        current_year = datetime.date.today().year
        age = current_year - birth_year

        return cls(name, age)
    
person1 = Person("John", 30)
person2 = Person.from_birth_year("Jane", 2000)

print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def pi():
        return 3.14159
    
result = MathUtils.add(5, 10)
print(f"The result is {result}")

print()

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)

        self.breed = breed

my_dog = Dog("Buddy", "Golder Retriever")
print(f"Name: {my_dog.name}, Breed: {my_dog.breed}")