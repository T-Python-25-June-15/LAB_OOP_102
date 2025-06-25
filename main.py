from bank_account import BankAccount

my_account = BankAccount("Ahmed", 100)

print("Account Holder:", my_account.get_account_holder())

print("Current Balance:", my_account.get_balance())
try:
    print("Depositing 50...")
    new_balance = my_account.deposit(50)
    print("New Balance:", new_balance)
except ValueError as e:
    print("Deposit Error:", e)
try:
    print("Withdrawing 30...")
    new_balance = my_account.withdraw(30)
    print("New Balance:", new_balance)
except Exception as e:
    print("Withdraw Error:", e)
try:
    print("Trying to withdraw 200...")
    new_balance = my_account.withdraw(200)
    print("New Balance:", new_balance)
except Exception as e:
    print("Withdraw Error:", e)

print("Final Balance:", my_account.get_balance())

