import sys
from bank_account import BankAccount

def main():
    # Create a bank account instance (initial balance of 0 by default)
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount> or display")
        return

    # Parse the command and arguments
    input_command = sys.argv[1].lower()

    if ":" in input_command:
        try:
            command, value = input_command.split(":")
            amount = float(value)
        except ValueError:
            print("Invalid format. Use <command>:<amount> (e.g., deposit:50).")
            return

        if command == "deposit":
            account.deposit(amount)
            account.display_balance()
        elif command == "withdraw":
            if account.withdraw(amount):
                account.display_balance()
        else:
            print("Unknown command. Use 'deposit', 'withdraw', or 'display'.")

    elif input_command == "display":
        account.display_balance()
    else:
        print("Unknown command. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")

if __name__ == "__main__":
    main()
