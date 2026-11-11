class Transaction:

    def deposit(self, account):
        amount = float(input("Enter amount to deposit: "))
        account["balance"] += amount
    from datetime import datetime

def deposit(self, account_number):

    amount = float(input("Enter deposit amount: "))

    timestamp = datetime.now()

    print("\nTransaction Successful")
    print(f"Amount Deposited: R{amount}")
    print(
        f"Date & Time: "
        f"{timestamp.strftime('%d/%m/%Y %H:%M:%S')}"
    )



    def withdraw(self, account):
        amount = float(input("Enter amount to withdraw: "))

        if amount > account["balance"]:
            return "Insufficient funds."
            return False
        account["balance"] -= amount
        return "Withdrawal successful."
        return f"New Balance: R{account['balance']}"
        return True

    def check_balance(self, account):
        return f"Current Balance: R{account['balance']}"
from datetime import datetime

def withdraw(self, account_number):

    amount = float(input("Enter withdrawal amount: "))

    timestamp = datetime.now()

    print("\nTransaction Successful")
    print(f"Amount Withdrawn: R{amount}")
    print(
        f"Date & Time: "
        f"{timestamp.strftime('%d/%m/%Y %H:%M:%S')}"
    )