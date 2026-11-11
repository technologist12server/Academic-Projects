from transaction import Transaction
import hashlib

#implement the login function
class Login:

    def login(self, accounts):

        account_number = int(input("Enter Account Number: "))
        pin = input(hashlib.sha256("Enter PIN: ".encode()).hexdigest() + ": ")

        if account_number in accounts:

            if accounts[account_number]["pin"] == pin:

                print("Login Successful")

                transaction = Transaction()

                while True:

                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    choice = input("Choose option: ")

                    if choice == "1":
                        transaction.deposit(accounts[account_number])

                    elif choice == "2":
                        transaction.withdraw(accounts[account_number])

                    elif choice == "3":
                        transaction.check_balance(accounts[account_number])

                    elif choice == "4":
                        print("Logged Out")
                        break

                    else:
                        print("Invalid option")

            else:
                print("Incorrect PIN")
                print("Login Failed")

        else:
            print("Account not found")
            print("Login Failed")
        return True
