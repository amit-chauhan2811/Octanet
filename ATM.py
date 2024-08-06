import time

print("Please insert Your Card")
time.sleep(5)
password = 1302
pin = int(input("Enter Your ATM Pin "))

balance = 5000
transaction_history = []

if pin == password:
    while True:
        print(
            """
            1 == Check balance
            2 == Withdraw balance
            3 == Deposit balance
            4 == Change PIN
            5 == Transaction history
            6 == Exit
            """
        )

        try:
            option = int(input("Please enter your choice "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("========================================")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount "))
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw_amount
                transaction_history.append(f"Withdrawn: {withdraw_amount}")
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
                print("========================================")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount "))
            balance += deposit_amount
            transaction_history.append(f"Deposited: {deposit_amount}")
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
            print("========================================")

        elif option == 4:
            new_pin = int(input("Enter your new PIN "))
            confirm_new_pin = int(input("Confirm your new PIN "))
            if new_pin == confirm_new_pin:
                password = new_pin
                transaction_history.append("PIN changed")
                print("PIN changed successfully")
                print("========================================")
            else:
                print("PINs do not match. Try again.")
                print("========================================")

        elif option == 5:
            print("Transaction history:")
            for transaction in transaction_history:
                print(transaction)
            print("========================================")

        elif option == 6:
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid option, please try again")
            print("========================================")

else:
    print("Wrong Pin. Please try again")
