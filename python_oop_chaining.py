class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_balance(self):
        print(f"You have {self.account_balance} in your account.")


michael = User("Michael", "michael@yahoo.com")
john = User("John", "johnnyj@gmail.com")
tim = User("Tim", "timmy@sleepytime.com")

michael.make_deposit(87.53).make_deposit(39.47).make_deposit(7276.01).make_withdrawl(100.00).display_balance()

john.make_deposit(1000).make_deposit(1122).make_withdrawl(1200).display_balance()

tim.make_deposit(5000).make_withdrawl(1570).make_withdrawl(3572).display_balance()

