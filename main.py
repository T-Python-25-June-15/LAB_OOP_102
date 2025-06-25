from bankaccount import BankAccount

personInfo = BankAccount("Ahmed",52020)

while True:
    print("""
        1- Balance
        2- Deposit
        3- Withdraw
        4- Account Holder Name
        5- Exit
    """)

    try:
        option = int(input("Enter your option: "))
        match option:
            case 1:
                print(f"Your Balance is: ${BankAccount.get_balance(personInfo)}")
            case 2:
                amount = int(input("Enter amount to deposit: "))
                BankAccount.deposit(personInfo, amount)
            case 3:
                amount = int(input("Enter amount to withdraw: "))
                BankAccount.withdraw(personInfo, amount)
            case 4:
                print(f"The Account holder name: {BankAccount.get_account_holder(personInfo)}")
            case 5:
                break
    except Exception as ex:
        print(f"Error: {ex}")