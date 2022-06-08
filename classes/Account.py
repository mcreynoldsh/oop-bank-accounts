import csv
class Account:
    def __init__(self,account_id, initial_balance, open_date):
        self.account_id = account_id
        if initial_balance < 0:
            raise Exception("Initial balance cannot be negative")
        self.balance = initial_balance/100
        self.open_date = open_date
        self.owner = None
        
    
    def __str__(self):
        return f"""
        Account ID: {self.account_id}
        Balance: ${'{:.2f}'.format(self.balance)}
        Owner: {self.owner}
        Open Date: {self.open_date}
        Account Type: {self.__class__.__name__}"""

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 0:
            raise Exception(f"Not enough funds to withdraw ${withdraw_amount}!")

        else:
            self.balance = self.balance - withdraw_amount

        return self.balance

    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            raise Exception("Deposit amount must be positive!")
        else:
            self.balance = self.balance + deposit_amount

        return self.balance     

    def set_owner(self, owner):
        self.owner = owner   
    
    
    def all_accounts(self):
        accounts=[]
        with open("/Users/huntermcreynolds/code/exercises/Week3/oop-bank-accounts/support/accounts.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                accounts.append(self(int(row["account_id"]),int(row["initial_balance"]),row["open_date"]))
        return accounts

    def find(self,id):
         with open("/Users/huntermcreynolds/code/exercises/Week3/oop-bank-accounts/support/accounts.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                if int(row["account_id"]) == int(id):
                    return  Account(int(row["account_id"]),int(row["initial_balance"]),row["open_date"])
            return "No matching ID"


