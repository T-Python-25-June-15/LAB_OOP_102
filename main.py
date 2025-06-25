from bankaccount import BankAccount

menu = '''
1. deposit
2. withdraw
3. show balance
4. exit
'''

acc01 = BankAccount('Hesham', 100)

while True:
    try:
        user_input = int(input(menu))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    match user_input:
        case 1:
            try:
                deposit = float(input("Enter deposit amount: "))
                acc01.deposit(deposit)
            except Exception as e:
                print(e)

        case 2:
            try:
                withdraw = float(input("Enter withdrawal amount: "))
                acc01.withdraw(withdraw)
            except Exception as e:
                print(e)

        case 3:
            acc01.get_balance()

        case 4:
            print('Goodbye')
            break

        case _:
            print("Invalid option. Please choose 1-4.")
