class User:
    def __init__(self, nameParam, balanceParam):
        self.name = nameParam
        self.account = balanceParam
    def make_withdrawal(self, amount):
        self.account = amount - self.account
        print(f"{self.name}, Balance ${self.account}")
    def make_deposit (self, amount):
        self.account = amount + self.account
        print(f"{self.name}, Balance ${self.account}")
    def display_user_balance(self, amount):
        self.account = amount
        print(f"{self.name}, Balance ${self.account}")
        
user1 = User("Brad", 500)
user2 = User("Joe", 5000)
user3 = User("Tammy", 10000)

user1.make_deposit(30) .make_deposit(50) .make_deposit(120) .make_withdrawal(100) .display_user_balance()

user2.make_deposit(30) .make_deposit(50) .make_withdrawal(120) .make_withdrawal(100) .display_user_balance()

user3.make_deposit(30) .make_withdrawal(50) .make_withdrawl(120) .make_withdrawal(100) .display_user_balance()


