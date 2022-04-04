class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        
    def transfer_money(self, amount, other):
        self.account_balance -= amount
        other.make_deposit(amount)
        print(f"First User: {self.name}, Balance: ${self.account_balance}")
        print(f"Second User: {other.name}, Balance: ${other.account_balance}")

# 3 Users
tony = User('Tony', 'tony@gmail.com')
apple = User('Apple', 'apple@gmail.com')
zack = User('Zack', 'zack@gmail.com')

# 1st user
# Make 3 deposits
tony.make_deposit(300)
tony.make_deposit(350)
tony.make_deposit(150)
# Withdrawal
tony.make_withdrawal(200)
# Display the balance
tony.display_user_balance()

# 2nd user
# Deposits
apple.make_deposit(200)
apple.make_deposit(300)
# Withdrawal
apple.make_withdrawal(200)
apple.make_withdrawal(150)
# Display the balance
apple.display_user_balance()

# 3rd user
# Deposit
zack.make_deposit(340)
# Withdrawal
zack.make_withdrawal(70)
zack.make_withdrawal(120)
zack.make_withdrawal(55)
# Display the balance
zack.display_user_balance()

# BONUS
tony.transfer_money(150, apple)