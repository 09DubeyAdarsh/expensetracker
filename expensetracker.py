import csv
import os

def create_expense_csv():
    header = ["Date", "Category", "Amount"]
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

def add_expense(date, category, amount):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def view_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(",".join(row))

# Check if the expenses.csv file exists, create one if not
if not os.path.isfile("expenses.csv"):
    create_expense_csv()

while True:
    print("\nExpense Tracker")
    print("----------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = input("Enter the amount: ")
        add_expense(date, category, amount)
        print("Expense added successfully!")

    elif choice == "2":
        print("\nExpense List:")
        view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")
