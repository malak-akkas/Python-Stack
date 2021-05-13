class user:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def make_withdrawal(self, amount):
        self.balance = self.balance - amount

    def display_user_balance(self):
        print(self.name+str(self.balance))

    def deposit_user_balance(self, amount):
        self.balance += amount

    def transfer_money_to(self, other_user, amount):
        self.balance = self.amount + self.other_user


amro = user(500, "amro")
malak = user(1000, "malak")
mohammed = user(2000, "mohammed")
amro.deposit_user_balance(10000)
amro.deposit_user_balance(10000)
amro.deposit_user_balance(10000)
amro.make_withdrawal(500)
amro.display_user_balance()
malak.deposit_user_balance(10000)
malak.deposit_user_balance(10000)
malak.make_withdrawal(500)
malak.make_withdrawal(500)
malak.display_user_balance()
mohammed.deposit_user_balance(10000)
mohammed.make_withdrawal(500)
mohammed.make_withdrawal(500)
mohammed.make_withdrawal(500)
mohammed.display_user_balance()
