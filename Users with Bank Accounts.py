from BankAccount import BankAccount

class user:
    def _int_(self, name, year_of_birth, balance=0):
        self.name = name
        self.year_of_birth = year_of_birth
        self.account = BankAccount()
    
    def make_withdrawal(self, amount) :
        return self.account.withdraw(amount)

    def display_user_balance(self) :
        print (f"{self.name} Balance is:", end=" ")

    def deposit(self,amount):
        self.account.deposit(amount)

    def transfer_money(self , other_user, amount):
        if self.make_withdrawal (amount):
            other_user.deposit(amount)
            return True
        return False