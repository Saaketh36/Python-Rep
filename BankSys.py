class BankAcc:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return amount
        else:
            print("Low Balance")
    def getBalance(self):
        return self.__balance
    def __str__(self):
        return f"Account Holder: {self.name} , Balance: {self.__balance}"
    
Account = BankAcc("Myself",10000)
Account.deposit(10000)
Account.withdraw(21000)
print(Account.getBalance())