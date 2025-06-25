#wasan alqahtani

from bank_account import BankAccount
try:
    user = BankAccount("")
    while True:
        #take the name from the user 
        print("Welcome to Banking Account System")
        print("-"*20)
        name = input("Please Enter Your Name: ")
        
        if len(name)<=0 or name.isdigit():
            print("Wrong entry name must be string")

        else:
            #set the name 
            user.set_accountHolder(name)
            print("-"*20)
            break

    while True:
        #print the menue
        print(f"\nWelcome {user.get_account_holder()} ")
        print("\n Menue")
        print("-"*20) 
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display your balanced")
        print("4. Exit")
        print("-"*20) 
        #take the option from the user
        option = input("Please choose number from menue above: ")
        match option:
            case "1":
                print("\nDeposit Operation")
                print("-"*20) 
                #take amount from user
                amount = input("please enter an amount to deposit: ")
                if amount.isnumeric():
                    #call deposite operation 
                    print(f"Your updated balanced is: {user.deposit(int(amount))}")
                else:
                    print("the amount must be nummber")

            case "2":
                print("\nWithdraw Opertation")
                print("-"*20)
                #take amount from the user
                amount = input("please enter an amount to withdraw: ")
                #call withdraw method
                balance = user.withdraw(int(amount))
                print(f"Your updated balanced is: {balance}")
                
                  

            case "3":
                #call get balanced
                print("\nDisplay your balanced account ") 
                print("-"*20)
                print(f"Your Balanced is: {user.get_balance()}")

            case "4":
                print("-"*20)
                print("GoodBye")
                break 

            case _:
                print("Wrong number try again")
                print("-"*20)
except Exception as e :
    print(e)
