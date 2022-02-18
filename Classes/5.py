class BankAccount(): 
    def __init__(self,owner,balance): 
        self.owner = owner 
        self.balance = balance 
    def deposit(self,money): 
        self.balance += money 
    def  withdraw(self,minus): 
        if minus < self.balance:  
            self.balance -= minus 
            print (self.balance) 
        else :  
            print("Not enough money")     
MyAcc= BankAccount("Yor acc:",int(input()))   
MyAcc.deposit(int(input())) 
print(MyAcc.balance) 
MyAcc.withdraw(int(input()))