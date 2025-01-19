class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount to the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds are available."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current balance: ${self.account_balance}")
