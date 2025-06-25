from bank import BankAccount

# create instance
person1= BankAccount("Sara")
person2 = BankAccount("Ahmad")

try:
    # display informations
    print(f"Account Holder: {person1.get_account_holder()}")
    print(f"Initial Balance: {person1.get_balance()}")
    print(f"Blance after deposit: {person1.deposit(100)}")
    print(f"Account holder: {person1.get_account_holder()}, Current balance: {person1.get_balance()}")
    print(f"Blance after withdraw :{person1.withdraw(50)}")
    print(f"Account holder: {person1.get_account_holder()}, Current balance: {person1.get_balance()}")
    print("-"*40)
    print(f"Account Holder: {person2.get_account_holder()}")
    print(f"Initial Balance: {person2.get_balance()}")
    print(f"Blance after deposit: {person2.deposit(1000)}")
    print(f"Account holder: {person2.get_account_holder()}, Current balance: {person2.get_balance()}")
    print(f"Blance after withdraw :{person2.withdraw(600)}")
    print(f"Account holder:{person2.get_account_holder()}, Current balance: {person2.get_balance()}")
    
except ValueError as e:
    print(e)

except Exception as e:
    print(e)


