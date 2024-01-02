class Account():
    def __init__(self,x,y):
        self.owner = x
        self.balance = y
    def deposit(self,x):
        self.balance = self.balance + x
        print("Deposit Accepted")
    def withdraw(self,x):
        if x > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance = self.balance - x
            print("withdrawal Accepted")
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
