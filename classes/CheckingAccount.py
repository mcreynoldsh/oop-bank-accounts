from Account import Account
class CheckingAccount(Account):
    def __init__(self,account_id, initial_balance, open_date):
        self.withdraw_count = 0
        parent_instance= super()
        parent_instance.__init__(account_id, initial_balance, open_date)
    
    def withdraw(self, withdraw_amount):
        withdraw_amount_fee = int(withdraw_amount) - 1
        if self.balance - withdraw_amount_fee < 0:
            raise Exception(f"Not enough funds to withdraw ${withdraw_amount} plus $1 fee!")

        else:
            self.balance = self.balance - withdraw_amount_fee

        return self.balance
    
    def withdraw_using_check(self,amount):

        if self.balance - amount < -10:
            raise Exception("Not enough funds, balance cannot be lower than -$10")
        elif self.withdraw_count >= 3:
            amount = amount + 2
            if self.balance - amount < -10:
                raise Exception("Not enough funds, balance cannot be lower than -$10 \n(transaction has $2 fee included)")
            else:
                self.balance = self.balance - amount
        else:
            self.withdraw_count = self.withdraw_count + 1
            self.balance = self.balance - amount
        return self.balance      

    def reset_checks(self):
        self.withdraw_count = 0  
    
    def all_accounts(self):
        return super().all_accounts(self)
