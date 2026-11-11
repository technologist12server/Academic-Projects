import csv
import hashlib
import random
import os

class Registration:

    def register(self):

        phone = input("Enter phone number:")

        # Validate phone number length and format
        if len(phone) != 10 or not phone.isdigit():
            print("Phone number must be 10 digits.")
            return

        if not phone.startswith("0"):
            print("Phone number must start with 0.")
            return

        file_name = "accounts.csv"

        # Create file with header if it doesn't exist
        if not os.path.exists(file_name):
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "account_number",
                    "phone",
                    "pin_hash",
                    "balance"
                ])

        existing_accounts = []
        existing_phones = []

        with open(file_name, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                existing_accounts.append(
                    row["account_number"]
                )

                existing_phones.append(
                    row["phone"]
                )

        # Check duplicate phone number
        if phone in existing_phones:
            print("Phone number already registered.")
            return

        # Generate unique account number
        while True:

            account_number = str(
                random.randint(10000000, 99999999)
            )

            if account_number not in existing_accounts:
                break

        # User creates PIN and hash it for storage
        pin = input(hashlib.sha256("Create a PIN (4-5 digits): ".encode()).hexdigest() + ": ")

        if not pin.isdigit():
            print("PIN must contain only numbers.")
            return

        if len(pin) < 4 or len(pin) > 5:
            print("PIN must be 4 or 5 digits.")
            return
#hash the PIN for confirmation
        confirm_pin = input(hashlib.sha256("Confirm PIN: ".encode()).hexdigest() + ": ")
        if confirm_pin != hashlib.sha256(pin.encode()).hexdigest():
            print("PINs do not match.")
            return

        # Hash PIN
        hashed_pin = hashlib.sha256(
            pin.encode()
        ).hexdigest()

        with open(file_name, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                account_number,
                phone,
                hashed_pin,])

        print("\nRegistration Successful")
        print(f"Account Number: {account_number}")
        print("PIN saved successfully.")