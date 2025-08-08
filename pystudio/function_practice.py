def greet_player(username="Player"):
    print(f"Welcome to the game, {username}!")
    print("Please follow the instructions on the screen.")


print("Starting the program...")
greet_player("CodeWizard")
greet_player()
print("Program finished.")

def add_numbers(num1, num2):
    print(f"Adding {num1} and {num2}...")
    sum_value = num1 + num2
    return sum_value
    print("This line will never run!")

result = add_numbers(10, 5)
print("The function finished.")
print("The result is:", result)
print("The result of another call is:", add_numbers(100, 2))


def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet(pet_name="Fido", animal_type="dog")

def create_character(name, level=1, class_type="Warrior"):
    print(name, level, class_type)

create_character("Rohan", class_type="Mage")

print()
print()
print()

player_level = 10

def level_up():
    player_level = 11
    print(f"Inside the function (local scope), the player is level: {player_level}")

print(f"Before the function call (global scope), the player is level: {player_level}")
level_up()
print(f"After the function call (global scope), the player is still level: {player_level}")