def greet(name):
    print(f"Hello, {name}!")

greet("Pythonista")

print()

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Fido")
describe_pet(pet_name="Fido", animal_type="dog")

print()

def create_character(name, class_type="Warrior"):
    print(f"Created {name}, the {class_type}.")

create_character("Rohan")
create_character("Sonia", "Mage")
create_character(class_type="Jatt", name="Rahul")

print()

def calculate_average(*numbers):
    return sum(numbers)/len(numbers)

print(calculate_average(10,20,30))
print(calculate_average(5,10,15,20))

print()

def build_profile(**user_info):
    for key, value in user_info.items():
        print(f"- {key}: {value}")

build_profile(name="Leo", age=30, city="New York")

print()

def format_name(first, last, /):
    print(f"{first} {last}")

format_name("Jane", "Doe")

print()

def sum_numbers(*numbers, precision):
    return round(sum(numbers), precision)

print(sum_numbers(1.23, 4.56, precision=3))

print()

def add(a, b):
    return a + b

sum_result = add(2, 3)
print(sum_result)

print()

def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")

print()

def greet_with_typed(name: str) -> None:
    print(f"Hello, {name}!")

greet_with_typed("Hnji")