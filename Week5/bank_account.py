class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("New Balance:", self.balance)
        else:
            print("Insufficient balance!")


# Create an object
account1 = BankAccount("Pedro Penduko", 2000)

# Test methods
account1.deposit(700)
account1.withdraw(400)