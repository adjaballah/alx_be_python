# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: The starting balance (default is 0).
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        :param amount: Amount to withdraw.
        :return: True if successful, False if insufficient funds.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")