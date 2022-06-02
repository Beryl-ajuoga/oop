class Account:
    def __init__(self ,name ,number , balance , bank_name):
        self.deposit = name
        self.withdraw = number
        self.withdraw = balance
        self.withdraw = bank_name
        

        

    def deposit(self,amount):
        self.balance+=amount
        return f"hello your current deposit is { self.deposit}"

    def withdraw(self,amount):
        self.balance+=amount
        return f"you'll be charged { self.withdraw} as the withdrawal amount "

   
