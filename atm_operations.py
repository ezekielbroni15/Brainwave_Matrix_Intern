def show_balance(balance):
    print("***************************")
    print(f"Your balance is ${balance:.2f}")
    print("***************************")

def deposit_money(balance):
    print("***************************")
    amount = float(input("Enter amount to be deposit: "))
    print("***************************")

    if amount <= 0:
        print("***************************")
        print("Sorry, that's not a valid amount.")
        print("***************************")
        return 0
    else:
        new_balance = balance + amount
        print(f"${amount} deposited successfully. New balance is ${new_balance}")
        if ask_print_receipt():
            print_receipt("Deposit", amount, new_balance)
        return amount

def withdraw_money(balance):
    print("***************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("***************************")

    if amount > balance:
        print("***************************")
        print("Sorry, Insufficient funds to withdraw.")
        print("***************************")
        return 0
    elif amount <= 0:
        print("***************************")
        print("Sorry, Amount must be greater than zero.")
        print("***************************")
        return 0
    else:
        new_balance = balance - amount
        print(f"${amount} withdrawn successfully. New balance is ${new_balance}")
        if ask_print_receipt():
            print_receipt("Withdraw", amount, new_balance)
        return amount

def print_receipt(transaction_type, amount, balance):
    print("***************************")
    print("         RECEIPT           ")
    print("***************************")
    print(f"Transaction: {transaction_type}")
    print(f"Amount: ${amount:.2f}")
    print(f"New Balance: ${balance:.2f}")
    print("***************************")

def ask_print_receipt():
    while True:
        choice = input("Do you want to print a receipt? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
