from Account import Account
class SavingsAccount(Account):
    def __init__(self,account_id, initial_balance, open_date):
        if initial_balance/100 < 10:
            raise Exception("Initial balance must be more than $10!")

        print(initial_balance/100)
        parent_instance= super()
        parent_instance.__init__(account_id, initial_balance, open_date)
    
    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 10:
            raise Exception(f"Not enough funds to withdraw ${withdraw_amount}, Savings must stay above $10!")

        else:
            self.balance = self.balance - withdraw_amount

        return self.balance

    def all_accounts(self):
        return super().all_accounts(self)
        
    def add_interest(self, rate):
        interest_amount = self.balance * rate/100
        self.balance += interest_amount
        return interest_amount