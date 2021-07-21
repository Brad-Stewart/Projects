class User:
    def __init__(self, firstNameParam, lastNameParam):
        self.firstName = firstNameParam
        self.lastName = lastNameParam
        self.bankAccount = bankAccount(int_rateParam=0.02, balanceParam=0)
    def display_user_balance(self):
        print(f"user name: {self.firstName} {self.lastName}; Account balance: {self.bankAccount}")
    def make_deposit(self, amount):
        self.bankAccount = self.bankAccount + amount
        return self
    def make_withdrawal(self, amount):
        self.bankAccount = self.bankAccount - amount
        return self

class bankAccount:
    def __init__(self, int_rateParam, balanceParam):
        self.balance = balanceParam
        self.int_rate = int_rateParam
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdrawal(self, amount):
        self.balance = self.balance - amount
        return self
    def balance(self, amount):
        self.balance = self.balance
        return self