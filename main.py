from bank import BankAccount


account1 = BankAccount("Hassan")

account1.deposit(500)
print(f"Account Holder: {account1.get_account_holder()}")
print(f"Account Balance: {account1.get_balance()}")

try:
    account1.withdraw(400)
    print("Withdrawal successful.")
    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Balance: {account1.get_balance()}")
except Exception as e:
    print(f"Withdrawal failed: {e}")
try:
    account1.withdraw(3000)
    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Balance: {account1.get_balance()}")
except Exception as e:
    print(f"Withdrawal failed: {e}")
    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Balance: {account1.get_balance()}")

try:
    account1.withdraw(-4000)
    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Balance: {account1.get_balance()}")
except Exception as e:
    print(f"Withdrawal failed: {e}")
