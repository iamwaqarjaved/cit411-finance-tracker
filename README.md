# CIT 411 Finance Tracker

## Repository Description

A Python command-line finance tracker that records income and expenses, validates user input, calculates a running balance, and prints a formatted ledger.

## Project Overview

This project is a command-line finance tracker built for CIT 411. The program allows a user to enter income and expense transactions, validates the input, calculates a running balance, and displays a formatted ledger using Python f-strings.

The goal of this lab is to practice the complete development workflow:

- Installing and verifying Python
- Setting up VS Code
- Creating a Python virtual environment
- Initializing a Git repository
- Writing and testing a Python command-line program
- Committing changes during development
- Pushing the project to GitHub
- Documenting the project with a README file

## Features

- Records income transactions
- Records expense transactions
- Validates transaction type
- Rejects negative or zero amounts
- Handles non-numeric input without crashing
- Rejects empty transaction descriptions
- Maintains a running balance
- Prints a formatted transaction ledger
- Uses Python functions for clean code organization
- Uses f-strings for formatted output

## Technologies Used

- Python 3.12+
- VS Code
- Python extension for VS Code
- Pylance extension for VS Code
- Git
- GitHub

## Project Structure

```text
cit411-finance-tracker/
│
├── tracker.py
├── README.md
├── .gitignore
└── .venv/
```

> Note: The `.venv/` folder should not be pushed to GitHub. It is ignored using `.gitignore`.

## Environment Setup

### Step 1: Install Python

Install Python 3.12 or higher from:

```text
https://www.python.org/downloads/
```

Do not use the Microsoft Store version of Python on Windows.

After installation, verify Python:

```bash
python --version
```

or on macOS/Linux:

```bash
python3 --version
```

Expected result:

```text
Python 3.12.x
```

## Step 2: Install VS Code

Install Visual Studio Code from:

```text
https://code.visualstudio.com/
```

Then install these VS Code extensions:

- Python
- Pylance

In VS Code, select the correct Python interpreter:

1. Open the project folder.
2. Press `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
3. Search for `Python: Select Interpreter`.
4. Select the Python interpreter from your `.venv` environment.

## Step 3: Create the Project Folder

### Windows PowerShell

```powershell
mkdir cit411-finance-tracker
cd cit411-finance-tracker
```

### macOS / Linux Terminal

```bash
mkdir cit411-finance-tracker
cd cit411-finance-tracker
```

## Step 4: Initialize Git

```bash
git init
```

This creates a new local Git repository.

## Step 5: Create a Virtual Environment

### Windows PowerShell

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux Terminal

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

After activation, the terminal should show something like:

```text
(.venv)
```

## Step 6: Create a `.gitignore` File

Create a file named `.gitignore` and add:

```gitignore
.venv/
__pycache__/
*.pyc
.vscode/
```

This prevents unnecessary local environment files from being pushed to GitHub.

## Program File

Create a file named:

```text
tracker.py
```

Paste the following code:

```python
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
```

## How to Run the Program

Make sure your virtual environment is activated.

Then run:

```bash
python tracker.py
```

or on macOS/Linux:

```bash
python3 tracker.py
```

## Sample Test Flow

Example user input:

```text
income
2500
Paycheck
expense
1200
Rent
expense
85.75
Groceries
income
150
Freelance work
q
```

Example output:

```text
======================================================================
                        FINANCE TRACKER LEDGER                        
======================================================================
#    Type        Description                       Amount     Balance
----------------------------------------------------------------------
1    Income      Paycheck                         $  2500.00 $   2500.00
2    Expense     Rent                             $ -1200.00 $   1300.00
3    Expense     Groceries                        $   -85.75 $   1214.25
4    Income      Freelance work                   $   150.00 $   1364.25
----------------------------------------------------------------------
                                             Current Balance: $   1364.25
======================================================================
```

## Input Validation

The program validates user input in the following ways:

### Transaction Type Validation

Accepted values:

```text
income
expense
q
```

Invalid values are rejected.

### Amount Validation

The amount must be:

- Numeric
- Greater than zero

Invalid examples:

```text
abc
-50
0
```

These values are rejected without crashing the program.

### Description Validation

The description cannot be empty.

Invalid example:

```text

```

If the user presses Enter without typing a description, the program asks again.

## Git Commit Workflow

The lab requires at least three commits during development.

### Commit 1: Initial Project Setup

After creating `.gitignore`:

```bash
git add .gitignore
git commit -m "Initial project setup with gitignore"
```

### Commit 2: Add Basic Program

After creating the first working version of `tracker.py`:

```bash
git add tracker.py
git commit -m "Add basic finance tracker loop"
```

### Commit 3: Add Validation and Ledger

After adding input validation and formatted ledger output:

```bash
git add tracker.py
git commit -m "Add input validation and formatted ledger"
```

### Commit 4: Add README

After creating this README file:

```bash
git add README.md
git commit -m "Add README with setup and run instructions"
```

## Check Commit History

Run:

```bash
git log --oneline
```

Example output:

```text
a7c2f90 Add README with setup and run instructions
9b4a2d1 Add input validation and formatted ledger
5f8d3aa Add basic finance tracker loop
1c3e92b Initial project setup with gitignore
```

Take a screenshot showing at least three commits.

## Create GitHub Repository

Create a private GitHub repository named:

```text
cit411-finance-tracker
```

Recommended repository description:

```text
CIT 411 Python command-line finance tracker for recording income and expenses with validation, running balance, and formatted ledger output.
```

Suggested GitHub topics:

```text
python
finance-tracker
command-line
cli
student-project
cit411
input-validation
```

## Push Code to GitHub

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cit411-finance-tracker.git
git push -u origin main
```

## Screenshot Requirements

Submit the following screenshots:

### 1. VS Code Running the Program

The screenshot should show:

- `tracker.py` open in VS Code
- Terminal running the program
- Sample income and expense transactions
- Final formatted ledger output

### 2. Git Log Screenshot

Run:

```bash
git log --oneline
```

The screenshot should show at least three commits.

### 3. GitHub Repository Screenshot

The screenshot should show:

- Repository name: `cit411-finance-tracker`
- Files uploaded:
  - `tracker.py`
  - `README.md`
  - `.gitignore`

## Final Submission Checklist

Before submitting, confirm:

- [ ] Python 3.12+ installed from python.org
- [ ] VS Code installed
- [ ] Python extension installed
- [ ] Pylance extension installed
- [ ] Project folder created
- [ ] Git initialized
- [ ] Virtual environment created
- [ ] `.gitignore` created
- [ ] `tracker.py` created
- [ ] Program accepts income transactions
- [ ] Program accepts expense transactions
- [ ] Program validates transaction type
- [ ] Program rejects negative or zero amounts
- [ ] Program handles non-numeric input
- [ ] Program rejects empty descriptions
- [ ] Program calculates running balance
- [ ] Program prints formatted ledger
- [ ] README file completed
- [ ] At least three Git commits created
- [ ] Code pushed to private GitHub repository
- [ ] VS Code screenshot captured
- [ ] Git log screenshot captured
- [ ] GitHub repository screenshot captured

## Repository Status

This project is complete when the working `tracker.py` file is committed to GitHub with at least three commits and the required screenshots are ready for submission.
