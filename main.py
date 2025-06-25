from Models import BankAccount

while True:
    print("\n" + "-" * 10 + "Bank System" + "-" * 10 + "\n") 
    try: 
        name = input("account holder: ")
        balance = float(input("balance: "))
        if balance == 0:
            new_bank_account = BankAccount(name)
            break
        else:
            new_bank_account = BankAccount(name, balance)
            break
            
    except Exception as e:
        print(e)
        
while True:
    print("1. deposit\n2. withdraw\n3. view balance\n4. view account holder\n5. exit\n")
    try:
        user_input = int(input("Enter your choice: "))
        match user_input:
            case 1: new_bank_account.deposit(float(input("Deposit: ")))
            case 2: new_bank_account.withdraw(float(input("withdraw: ")))
            case 3: print(new_bank_account.getBalance())
            case 4: print(new_bank_account.getAccountHolder())
            case 5: break
            case _: print("invalid choice, please try again")
    except Exception as e:
        print(e)
    finally:
        input("...")
    
    