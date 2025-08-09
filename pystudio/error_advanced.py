import traceback

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Only ${self.balance} available.")
        self.balance -= amount
        return self.balance
    
my_account = BankAccount(100)

try:
    my_account.withdraw(500)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

print()

def load_data_from_network():
    raise ConnectionError("Failed to connect to the server.")

def get_user_profile():
    try:
        load_data_from_network()
    except ConnectionError as e:
        raise RuntimeError("Could not retrieve user profile.") from e

try:
    get_user_profile()
except RuntimeError as e:
    print(f"Caught an error: {e}")

    print("\n--- DEVELOPER TRACEBACK ---")
    traceback.print_exc()
    print("-----------------------------")

print()

# get_user_profile()

