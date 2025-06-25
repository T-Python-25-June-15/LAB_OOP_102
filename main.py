from bank import BankAccount
def main():
    account = BankAccount("ahmad",1700)
    print("account holde is: ", account.get_account_holder())
    print("balnce is : ", account.get_balance())

    account.deposit(100)
    print("balance is ", account.get_balance())

    try:
        account.withdraw(1000)
        print("balance is: ",account.get_balance())
    except Exception as e:
        print("error! " ,e)

    try:
        account.withdraw(3000)
        print("balance is: ",account.get_balance())
    except Exception as e:
        print("error! " ,e)
    

    print("balance is: ", account.get_balance())

main()