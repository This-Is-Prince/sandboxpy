secret_number = 7
guess = 0
print("--- Guess the number between 1 and 10! ---")

while guess != secret_number:
    guess_text = input("Enter your guess:")
    guess = int(guess_text)

    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    else:
        print("Yes you are right about it.")

print(f"You got it! The secret number was {secret_number}")