# backend/savings_account.py

from backend.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Savings account with interest feature"""

    def __init__(self, account_no, name, balance=0):
        super().__init__(account_no, name, balance)
        self.interest_rate = 0.05  # 5% interest

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"💰 Interest of ₹{interest} added.")
