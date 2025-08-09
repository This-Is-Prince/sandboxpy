class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread
        print(f"A new dog named {self.name} has been created!")

    def bark(self):
        return f"{self.name} says: Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Poodle")

print(f"{dog1.name} is a {dog1.bread}.")
print(f"{dog2.name} is a {dog2.bread}.")

print(dog1.bark())
print(dog2.bark())

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._is_engine_on = False
        self._speed = 0

    def start_engine(self):
        self._is_engine_on = True
        print("Engine started.")
    
    def accelerate(self):
        if self._is_engine_on:
            self._speed += 10
            print(f"Accelerating. Current speed: {self._speed} mph.")
        else:
            print("Cannot accelerate. The engine is off.")

print()

class Animal:
    def __init__(self, name):
        self.name = name;

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
    
class Dog1(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

my_dog = Dog1("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak())
print(my_cat.speak())