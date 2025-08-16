# Expense Tracker - CLI Application

expenses = {}  # Structure: {"Category": [amount1, amount2, ...]}

def add_expense():
    category = input("Enter expense category (e.g., Food, Entertainment, Utilities): ").strip().title()
    try:
        amount = float(input("Enter amount spent: ").strip())
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    expenses.setdefault(category, []).append(amount)
    print(f"Added ₹{amount:.2f} under '{category}' category.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    for category, amounts in expenses.items():
        print(f"{category}: {', '.join(f'₹{amt:.2f}' for amt in amounts)}")
    print("---------------------")

def expense_summary():
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(sum(amounts) for amounts in expenses.values())
    count = sum(len(amounts) for amounts in expenses.values())
    average = total / count if count else 0

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")
    print("\nCategory-wise Total:")
    for category, amounts in expenses.items():
        print(f"{category}: ₹{sum(amounts):.2f}")
    print("-----------------------")

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the program
menu()
