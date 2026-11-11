import logging
from menu import Menu
from registration import Registration
from login import Login

accounts = {}
logger = logging.getLogger(__name__)
menu = Menu()
registration = Registration()
login = Login()
while True:

    menu.display()

    choice = input("Select option: ")

    if choice == "1":

        registration.register()

    elif choice == "2":

        login.login(accounts)

    elif choice == "3":
        logger.info("Exiting...")
        break

    else:
        logger.warning("Invalid option.")