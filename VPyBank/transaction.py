class Transaction:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: R"))
        self.balance += amount
        print(f"Deposit successful. New balance: R{self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: R"))

        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: R{self.balance}")

    def check_balance(self):
        print(f"Your account balance is: R{self.balance}")

    def menu(self):
        print("\n--- Transaction Menu ---")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Account Balance")

        choice = input("Select an option: ")

        if choice == "1":
            self.withdraw()

        elif choice == "2":
            self.deposit()

        elif choice == "3":
            self.check_balance()

        else:
            print("Invalid option selected.")

if __name__ == "__main__":
    account = Transaction(1000)  # Starting balance
    account.menu()
