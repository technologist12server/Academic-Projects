import hashlib

class AccountLogin:
    storage = {}

    def __init__(self, phone_number, pin):
        self.phone_number = phone_number
        self.pin = pin

    def login(self):
        if self.phone_number not in AccountLogin.storage:
            print("Phone number not found.")
            return False

        hashed_pin = hashlib.sha256(self.pin.encode()).hexdigest()

        if AccountLogin.storage[self.phone_number]["pin"] == hashed_pin:
            print("Login successful.")
            return True
        else:
            print("Incorrect PIN.")
            return False


phone_number = input("Enter phone number: ")
pin = input("Enter PIN: ")

account_login = AccountLogin(phone_number, pin)
account_login.login()
