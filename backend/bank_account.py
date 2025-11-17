# backend/bank_account.py

class BankAccount:
    """Base Bank Account class"""

    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"💸 Withdrew ₹{amount}")
        else:
            print("❌ Insufficient balance!")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Account: {self.account_no} | Name: {self.name} | Balance: ₹{self.balance}")
