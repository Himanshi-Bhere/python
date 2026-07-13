# menu should be keep appearing until user selects exit option

initial_balance = 50000.0

while True:
    print("\n Welcome to the ATM simulator!")
    print("Please select an option: ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option =input("Enter your option (1-4): ")
    if option == "1":
        print(f"Current Balance: ${initial_balance}")
    elif option == "2":
        deposit_amount = float(input("Enter deposit amount: "))
        initial_balance += deposit_amount
        print(f"Updated balance after deposit: ${initial_balance}")
    elif option == "3":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        if withdraw_amount <= initial_balance:
            initial_balance -= withdraw_amount
            print(f"Withdrawal successful. Updated balance: ${initial_balance}")
        else:
            print("Insufficient balance.")
    elif option == "4":
        print("Thank you for using our ATM.")
        break
    else:
        print("Invalid option. Please select a valid option (1-4).")

            
            
