class Menu:
    def __init__(self):
        pass

    def display(self):
        print("Welcome to VPyBank! Select an option from the menu below:")
        print("1. Login")
        print("2. Register")
        print("3. Transaction")
        print("4. Exit")

    def options(self, choice):
        if choice == "1":
            print("Redirecting to Login...")
            # login()

        elif choice == "2":
            print("Redirecting to Registration...")
            # register()

        elif choice == "3":
            print("Redirecting to Transaction...")
            # transaction()

        elif choice == "4":
            print("Thank you for using VPyBank.")
            exit()

        else:
            print("Invalid option selected.")


if __name__ == "__main__":
    menu = Menu()
    menu.display()

    choice = input("You have selected option: ")
    menu.options(choice)
