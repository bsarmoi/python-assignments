import json
import os
import matplotlib.pyplot as plt

# Define the initial variables
income = 0.0
expenses = 0.0
savings = 0.0
transactions = []

# Function to print the welcome message
def print_welcome():
    print("Welcome to the Personal Finance Tracker!")
    print("You can use this tool to manage your income, expenses, and savings.")
    print("Instructions:")
    print("1. Add income")
    print("2. Add expenses")
    print("3. View reports")
    print("4. Exit")

# Function to get valid float input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get valid user option
def get_valid_option():
    while True:
        option = input("Choose an option: ")
        if option in ['1', '2', '3', '4']:
            return option
        else:
            print("Invalid option. Please try again.")

# Function to add income
def add_income():
    global income
    amount = get_valid_float("Enter income amount: ")
    description = input("Enter income description: ")
    transaction = {
        "type": "income",
        "amount": amount,
        "description": description
    }
    transactions.append(transaction)
    income += amount

# Function to add expense
def add_expense():
    global expenses
    amount = get_valid_float("Enter expense amount: ")
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "description": description
    }
    transactions.append(transaction)
    expenses += amount

# Function to calculate savings
def calculate_savings():
    global savings
    savings = income - expenses

# Function to view reports
def view_reports():
    print("\nTransaction Report:")
    for transaction in transactions:
        print(transaction)
    calculate_savings()
    print(f"\nTotal Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Total Savings: {savings}")
    report_by_category()
    plot_expenses()

# Function to generate report by category
def report_by_category():
    category_totals = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    print("\nExpense Report by Category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

# Function to plot expenses by category
def plot_expenses():
    categories = []
    amounts = []
    for transaction in transactions:
        if transaction["type"] == "expense":
            categories.append(transaction["category"])
            amounts.append(transaction["amount"])
    if categories and amounts:
        plt.bar(categories, amounts)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()
    else:
        print("No expenses to display.")

# Function to save transactions to a file
def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

# Function to load transactions from a file
def load_transactions():
    global transactions, income, expenses
    if os.path.exists('transactions.json'):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
            for transaction in transactions:
                if transaction["type"] == "income":
                    income += transaction["amount"]
                elif transaction["type"] == "expense":
                    expenses += transaction["amount"]
    else:
        transactions = []

# Main program loop
def main():
    load_transactions()
    print_welcome()

    while True:
        user_choice = get_valid_option()
        if user_choice == '1':
            add_income()
        elif user_choice == '2':
            add_expense()
        elif user_choice == '3':
            view_reports()
        elif user_choice == '4':
            save_transactions()
            print("Thank you for using the Personal Finance Tracker!")
            break

if __name__ == "__main__":
    main()
