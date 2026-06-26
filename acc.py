class AccountHolder:
    def __init__(self,name,email):
        self.name = name
        self.email = email

class BankAccount:

    bank_name = "World bank"
    
    def __init__(self,balance,name,email):
        self.__balance = balance if balance > 0 else 0
        self.accountholder = AccountHolder(name,email)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
       if amount > 0:
           self.__balance = amount
       else:
           print("Invalid amount")
           self.__balance = 0

    def deposit(self,amount):
        if amount > 0:
           self.__balance += amount
           print("After Deposit =",self.__balance,)
        else:
           print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
           print("Invalid Withdraw amount")
        else:
           self.__balance -= amount
           print("After withdraw =",self.__balance)

    def display(self):
        return (f"Account Holder = {self.accountholder.name}\n"
                f"Email = {self.accountholder.email}\n"
                f"Balance = {self.balance}"  )
         
    @classmethod
    def show_bank_name(cls):
        print("Bank name =",cls.bank_name)
        

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def __str__(self): 
        return f"{self.accountholder.name} - {self.balance}"
        
b1 = BankAccount(5000,"Ali","ts895994@gmailcom")

b1.show_bank_name()
print()
print(b1.display())
print()
b1.deposit(2000)
print()
b1.withdraw(1000)
print()
print(b1)
print()
print(b1.is_valid_amount(1000))
print(b1.is_valid_amount(-1000))