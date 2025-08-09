try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero! Setting result to None.")
    result = None


print(f"The program continues. The result is {result}.")

print()

try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found. Please check the path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print()

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print(f"Success! The result is {result}.")
finally:
    print("Execution finished.")

print()

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age(25)
    set_age(-5)
except ValueError as e:
    print(f"Error setting age: {e}")

print()