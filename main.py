from BankAccount import BankAccount

person = BankAccount("ahmed", 50)

print("WELCOME TO BANK ACCOUNT SYSTEM")
print("1- Deposit\n2- Withdraw\n3- Check balance\n4- Display account holder name")
choice = input("Choose from the above list, or exit: ")

while True:
    match choice:
        case '1':
            try:
                amount = int(input("Enter the amount to deposit: "))
                person.deposit(amount)
                print(f"Deposit successfully. The current balance: {person.get_balance()}")
            except Exception as e:
                print(e)
        case '2':
            try:
                amount = int(input("Enter the amount to withdraw: "))
                person.withdraw(amount)
                print(f"Withdraw successfully. The current balance: {person.get_balance()}")
            except Exception as e:
                print(e)
        case '3':
            print(f"Your balance is: {person.get_balance()}")
        case '4':
            print(f"The account holder name is {person.get_account_holder()}")
        case 'exit':
            break
        case _:
            print("Invalid choice input")
            break
    input('press Enter to continue....\n')
    print("1- Deposit\n2- Withdraw\n3- Check balance\n4- Display account holder name")
    choice = input("Choose from the above list, or exit: ")

print('Thanks for using bank account system, Good Bye...')