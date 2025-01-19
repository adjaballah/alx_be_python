import argparse
from bank_account import BankAccount

def main():
    # Initialiser le compte bancaire avec un solde de départ (par défaut 0)
    account = BankAccount()

    # Définir les arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Bank Account Operations")
    parser.add_argument("action", help="Action to perform (deposit, withdraw, balance)")
    parser.add_argument("amount", type=float, nargs="?", default=0, help="Amount for deposit or withdrawal")

    # Analyser les arguments
    args = parser.parse_args()

    # Exécuter l'action demandée
    if args.action == "deposit":
        account.deposit(args.amount)
    elif args.action == "withdraw":
        account.withdraw(args.amount)
    elif args.action == "balance":
        account.display_balance()
    else:
        print("Invalid action. Please choose 'deposit', 'withdraw', or 'balance'.")

if __name__ == "__main__":
    main()
