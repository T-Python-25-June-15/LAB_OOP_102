class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def get_account_holder(self) -> str:
        return self.__account_holder

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. Account balance: ${self.__balance:.2f}")
