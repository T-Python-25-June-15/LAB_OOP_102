#wasan alqahtani
class BankAccount:
    #initialization 
    def __init__(self, account_holder:str, initial_balance:int=0 ) -> None:
        self.__account_holder = account_holder
        self.___initial_balance = initial_balance
    
    #create setters and getters for the private attributes
    def set_accountHolder(self, account_holder):
        self.__account_holder = account_holder

    def set_InitialBalanced(self, initial_balance):
           self.___initial_balance = initial_balance

    #deposite method
    def deposit(self,amount:int) ->int:
        '''this method takes the amount and added to the balanced and then
          return it to the user'''
        if amount >0:
            self.set_InitialBalanced(self.get_balance()+amount)
            return self.get_balance()
        
        else:
            print("The amount must be grater than 0")    

    #withdraw method    
    def withdraw(self,amount:int)-> int:
        '''this method takes amount and then subtract from the 
        balanced and then return it to the user'''
        #check if the amount number
        if not isinstance(amount, int):
            raise Exception ("the amount must be a number")
        #check if the amount is greater than balanced then raise exception
        if amount > self.get_balance():
            raise Exception ("there are insufficient funds")
        else:
             self.set_InitialBalanced(self.get_balance()-amount)
             return self.get_balance()
    #get the varibels
    def get_balance(self):
        return self.___initial_balance

    def get_account_holder(self):
        return self.__account_holder 

    

    

