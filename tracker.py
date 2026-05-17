"""
CIT 411 Finance Tracker

A simple command-line finance tracker that records income and expense
transactions, validates user input, calculates a running balance, and
prints a formatted ledger.
"""


def get_transaction_type():
    """Prompt user for transaction type and validate income/expense."""
    while True:
        transaction_type = input("Enter transaction type (income/expense) or 'q' to quit: ").strip().lower()

        if transaction_type == "q":
            return "q"

        if transaction_type in ["income", "expense"]:
            return transaction_type

        print("Invalid transaction type. Please enter 'income', 'expense', or 'q'.")


def get_amount():
    """Prompt user for amount and validate numeric positive input."""
    while True:
        amount_input = input("Enter amount: ").strip()

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def get_description():
    """Prompt user for a non-empty transaction description."""
    while True:
        description = input("Enter description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")


def print_ledger(transactions, balance):
    """Print a formatted ledger using f-strings."""
    print("\n" + "=" * 70)
    print(f"{'FINANCE TRACKER LEDGER':^70}")
    print("=" * 70)
    print(f"{'#':<5}{'Type':<12}{'Description':<30}{'Amount':>10}{'Balance':>12}")
    print("-" * 70)

    running_balance = 0.0

    for index, transaction in enumerate(transactions, start=1):
        if transaction["type"] == "income":
            running_balance += transaction["amount"]
            signed_amount = transaction["amount"]
        else:
            running_balance -= transaction["amount"]
            signed_amount = -transaction["amount"]

        print(
            f"{index:<5}"
            f"{transaction['type'].title():<12}"
            f"{transaction['description']:<30}"
            f"${signed_amount:>9.2f}"
            f"${running_balance:>11.2f}"
        )

    print("-" * 70)
    print(f"{'Current Balance:':>57} ${balance:>10.2f}")
    print("=" * 70)


def main():
    """Main program loop."""
    transactions = []
    balance = 0.0

    print("Welcome to the CIT 411 Finance Tracker")
    print("Enter your transactions below.")
    print("Type 'q' when you are finished.\n")

    while True:
        transaction_type = get_transaction_type()

        if transaction_type == "q":
            break

        amount = get_amount()
        description = get_description()

        if transaction_type == "income":
            balance += amount
        else:
            balance -= amount

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
        }

        transactions.append(transaction)

        print(f"Transaction added. Current balance: ${balance:.2f}\n")

    if transactions:
        print_ledger(transactions, balance)
    else:
        print("No transactions were entered.")

    print("\nThank you for using the Finance Tracker.")


if __name__ == "__main__":
    main()