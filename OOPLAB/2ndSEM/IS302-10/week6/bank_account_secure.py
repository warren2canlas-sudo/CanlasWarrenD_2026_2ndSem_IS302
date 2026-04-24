class BankAccount:
    def __init__(self, apd_balance):
        # Private attribute to keep the money safe
        self.__apd_balance = apd_balance

    def deposit(self, apd_amount):
        # Adds money to the private balance
        if apd_amount > 0:
            self.__apd_balance += apd_amount
            print(f"Deposited: {apd_amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, apd_amount):
        # Checks if there's enough money before deducting
        if apd_amount <= self.__apd_balance:
            self.__apd_balance -= apd_amount
            print(f"Withdrawn: {apd_amount}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        # The only way to view the balance
        return self.__apd_balance

# Creating an instance of the bank account
apd_account = BankAccount(5000)

# Performing transactions
apd_account.deposit(1000)
apd_account.withdraw(2000)

# Checking the final balance
print("Current Balance:", apd_account.get_balance())