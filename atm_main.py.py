#ATM

from atm_operations import show_balance, deposit_money, withdraw_money

def main():
    trials = 3
    user_debit_card = "1234567890123456"
    user_pin = 1234
    balance = 0
    is_running = True

    while trials != 0:
        print("***************************")
        print("  Welcome to Access Bank!  ")
        print("***************************")

        card_number = input("Please Enter your Debit Card Number: ")
        print("***************************")

        if card_number != user_debit_card:
            print("Invalid Debit Card Number. Please try again.")
            continue

        pin = int(input("Please Enter your four ATM Pin Number: "))
        print("***************************")

        if pin != user_pin:
            trials -= 1
            print(f"Wrong Pin Number, You Have {trials} Trials Left")
        else:
            while is_running:
                print("***************************")
                print(" Please choose an option: ")
                print("***************************")
                print("1. Show Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")
                print("***************************")

                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    show_balance(balance)
                elif choice == "2":
                    balance += deposit_money(balance)
                elif choice == "3":
                    balance -= withdraw_money(balance)
                elif choice == "4":
                    is_running = False
                else:
                    print("***************************")
                    print("That is an Invalid choice")
                    print("***************************")
            print("***************************")
            print("Thank you for using Access Bank!")
            print("***************************")
            break

if __name__ == "__main__":
    main()
