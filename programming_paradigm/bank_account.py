import json

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        self._account_balance += amount
        self.save_balance()
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            self.save_balance()
            return f"Withdrew: ${amount}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self._account_balance}"

    def save_balance(self):
        with open('balance.json', 'w') as f:
            json.dump({'balance': self._account_balance}, f)

    def load_balance(self):
        try:
            with open('balance.json', 'r') as f:
                data = json.load(f)
                self._account_balance = data.get('balance', 0)
        except FileNotFoundError:
            self._account_balance = 0
