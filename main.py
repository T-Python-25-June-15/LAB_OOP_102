from bank_account import BankAccount

account = BankAccount("Lama", 1000.0)

print(f"Account holder: {account.get_account_holder()}")
print(f"Current balance: {account.get_balance()}")

try:
    account.deposit(200)
    print(f"Balance after deposit: {account.get_balance()}")

    account.withdraw(500)
    print(f"Balance after withdrawal: {account.get_balance()}")

    account.withdraw(1000)  

except Exception as e:
    print("Error:", e)
