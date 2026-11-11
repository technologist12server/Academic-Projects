from menu import Menu
from Registration import AccountReg
from AccountLogin import AccountLogin

accounts = {}

menu = Menu()
registration = AccountReg()
login = AccountLogin()

while True:

    menu.display()

    choice = input("Select option: ")

    if choice == "1":

        registration.register(accounts)

    elif choice == "2":

        login.login(accounts)

    elif choice == "3":

        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid option.")


if __name__ == "__main__":
    menu = Menu()
    menu.display()

    choice = input("You have selected option: ")
    print("You have selected option:", choice)

    menu.options(choice)