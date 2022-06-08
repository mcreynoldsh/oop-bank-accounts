from Account import Account
from Owner import Owner
from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount
import csv
class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = CheckingAccount.all_accounts(CheckingAccount)
        self.owners = Owner.all_owners()
        self.connect_accounts_owners()

    def __str__(self):
        return_str = ""
        for x in self.accounts:
            return_str+= "\n" + str(x)
        return return_str    
    def connect_accounts_owners(self):
        id_list = []
        with open("/Users/huntermcreynolds/code/exercises/Week3/oop-bank-accounts/support/account_owners.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                id_list.append([row["account_id"],row["owner_id"]])
        for x in id_list:
            for account in self.accounts:
                for owner in self.owners:
                    if owner.owner_id == int(x[1]) and account.account_id == int(x[0]):
                        account.set_owner(owner)

bank = Bank("Capital Bank")
print(bank)
        