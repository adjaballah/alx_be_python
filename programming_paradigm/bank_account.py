class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialiser le compte bancaire avec un solde initial (par défaut à 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Déposer un montant spécifié sur le compte."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Retirer un montant spécifié du compte si les fonds sont suffisants."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")
        return False

    def display_balance(self):
        """Afficher le solde actuel."""
        print(f"Current balance: ${self.account_balance}")
