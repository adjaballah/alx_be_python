import sys
from bank_account import BankAccount

def main():
    account = BankAccount()
    account.load_balance()

    if len(sys.argv) != 2:
        print("Usage: python main-0.py <command>:<amount>")
        return

    command = sys.argv[1]
    if command.startswith("deposit:"):
        amount = int(command.split(":")[1])
        print(account.deposit(amount))
    elif command.startswith("withdraw:"):
        amount = int(command.split(":")[1])
        print(account.withdraw(amount))
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
