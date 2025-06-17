import os

# Represents a single expense entry.
class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    # Converts the Expense object to a CSV string for file storage.
    def to_csv(self):
        return f"{self.amount},{self.category},{self.description}\n"

    # Creates an Expense object from a CSV string.
    @staticmethod
    def from_csv(csv_line):
        amount, category, description = csv_line.strip().split(',', 2)
        return Expense(float(amount), category, description)

# Tracks and manages multiple expenses, saving and loading them from a file.
class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []             # List to store Expense objects.
        self.filename = filename       # File to save/load expenses.
        self.load_expenses()           # Load existing expenses when initialized.

    # Adds a new expense and saves the updated list to the file.
    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_expenses()           # Save changes right after adding.
        print('Expense added successfully!')

    # Displays all stored expenses.
    def view_expenses(self):
        if self.expenses:
            print('Expenses:')
            for index, expense in enumerate(self.expenses, 1):
                print(f'{index}. Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}')
        else:
            print('No expenses to display.')

    # Calculates and displays the total amount of all expenses.
    def calculate_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f'Total expenses: {total}')

    # Saves all expenses to the file in CSV format.
    def save_expenses(self):
        with open(self.filename, 'w') as f:
            for expense in self.expenses:
                f.write(expense.to_csv())

    # Loads expenses from the file, if it exists.
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.expenses = [Expense.from_csv(line) for line in f if line.strip()]

# Main program logic: menu and user interaction loop.
if __name__ == "__main__":
    tracker = ExpenseTracker()  # Create an ExpenseTracker instance.

    while True:
        print('Expense Tracker')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Calculate Total Expenses')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            category = input('Enter category: ')
            description = input('Enter description: ')
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.calculate_total_expenses()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')