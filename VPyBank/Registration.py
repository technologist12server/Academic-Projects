import random
import hashlib

class AccountReg:
    storage = {}
    used_account_numbers = set()

    def __init__(self, phone_number, pin):
        self.phone_number = phone_number
        self.pin = pin
        self.account_number = None

    def hash_pin(self):
        return hashlib.sha256(self.pin.encode()).hexdigest()

    def register(self):
        if self.phone_number in AccountReg.storage:
            print("Phone number already registered.")
            return False

        hashed_pin = self.hash_pin()

        AccountReg.storage[self.phone_number] = {
            "account_number": self.generate_account_number(),
            "pin": hashed_pin
        }

        self.account_number = AccountReg.storage[self.phone_number]["account_number"]

        print("Registration successful.")
        return True

    @staticmethod
    def pin_strength(pin):
        if len(pin) not in (4, 5):
            return "Pin must be 4 or 5 digits long."
        elif not pin.isdigit():
            return "Pin should contain only digits."
        else:
            return "Pin generated successfully."

    def generate_account_number(self):
        account_number = random.randint(1000000000, 9999999999)

        while account_number in AccountReg.used_account_numbers:
            account_number = random.randint(1000000000, 9999999999)

        AccountReg.used_account_numbers.add(account_number)

        return account_number


if __name__ == "__main__":
    print("-------Welcome to the registration page.-------")

    phone_number = input("Phone number: ")

    if not phone_number.startswith("0"):
        print("Phone number must start with 0.")
        exit()

    print("Pin must be 4 or 5 digits long.")
    pin = input("Generate pin: ")

    result = AccountReg.pin_strength(pin)
    print(result)

    if result != "Pin generated successfully.":
        exit()

    account = AccountReg(phone_number, pin)

    if account.register():
        print("Your account number is:", account.account_number)

        print("\nStored Account Data:")
        print(AccountReg.storage)

    print("Press 0 to return to the main menu.")
    return_to_menu = input("Enter choice: ")

    if return_to_menu == "0":
        print("Returning to main menu...")
    else:
        print("Invalid choice. Returning to main menu...")