class Account:
    def __init__(self ,name ,acc_number):
        self.name = name
        self.acc_number =acc_number
        self.balance = 0
        self.deposits=[]
        self.withdrawal=[]

      
    def deposit(self , amount):
        if amount <= 0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance +=amount
            self.deposits.append(amount)
            return f"You've deposited {amount}.Your new balance is {self.balance}" ,self.deposits


    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance is {self.balance}.You cannot withdraw the {amount}"
        elif amount <=0:
            return f"Amount must be greater than zero"
        else:
            self.balance -=amount
            self.withdrawal.append(amount)
            return f"You have withdrawn {amount} your balance is {self.balance}",self.withdrawal   

    def deposit_statement(self) :
        print(*self.deposits,sep="\n")

    def withdrawal_statement(self) :
        print(*self.deposits,sep="\n")
                   
        






   
