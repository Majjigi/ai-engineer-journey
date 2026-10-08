import argparse
import json
from pathlib import Path


FILE_PATH = Path(__file__).with_name("expenses.json")


def normalize_expense(expense):
    if not isinstance(expense, dict):
        return {"name": "Unknown", "amount": 0.0}

    name = expense.get("name") or expense.get("description") or "Unknown"
    amount = expense.get("amount", 0)
    return {"name": str(name), "amount": float(amount)}


def load_expenses():
    if not FILE_PATH.exists():
        return []

    with FILE_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    expenses = data.get("expenses", [])
    normalized_expenses = [normalize_expense(expense) for expense in expenses]

    if normalized_expenses != expenses:
        save_expenses(normalized_expenses)

    return normalized_expenses


def save_expenses(expenses):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump({"expenses": expenses}, file, indent=2)
        file.write("\n")


def add_expense(name, amount):
    name = str(name).strip()
    if not name:
        raise ValueError("Expense name cannot be empty.")

    try:
        amount_value = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a number.") from None

    if amount_value < 0:
        raise ValueError("Amount cannot be negative.")

    expenses = load_expenses()
    expense = {"name": name, "amount": round(amount_value, 2)}
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses saved.")
        return []

    print("Expenses:")
    for index, expense in enumerate(expenses, start=1):
        name = expense.get("name", "Unknown")
        amount = float(expense.get("amount", 0))
        print(f"{index}. {name}: ${amount:.2f}")
    return expenses


def delete_expense(index):
    expenses = load_expenses()

    try:
        position = int(index) - 1
    except ValueError as exc:
        raise ValueError("Expense number must be an integer.") from exc

    if position < 0 or position >= len(expenses):
        raise IndexError("Expense number is out of range.")

    removed = expenses.pop(position)
    save_expenses(expenses)
    return removed


def show_total():
    expenses = load_expenses()
    total = sum(float(expense.get("amount", 0)) for expense in expenses)
    print(f"Total: ${total:.2f}")
    return round(total, 2)


def interactive_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. List all expenses")
        print("3. Delete expense")
        print("4. Show total")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Expense name: ").strip()
            amount = input("Expense amount: ").strip()
            try:
                expense = add_expense(name, amount)
                print(f"Added: {expense['name']} - ${expense['amount']:.2f}")
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            list_expenses()
            if not load_expenses():
                continue
            expense_number = input("Enter the number to delete: ").strip()
            try:
                removed = delete_expense(expense_number)
                print(f"Deleted: {removed['name']} - ${float(removed['amount']):.2f}")
            except (ValueError, IndexError) as exc:
                print(f"Error: {exc}")

        elif choice == "4":
            show_total()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


def build_parser():
    parser = argparse.ArgumentParser(description="Manage personal expenses saved in expenses.json.")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("name")
    add_parser.add_argument("amount")

    subparsers.add_parser("list", help="List all expenses")
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by number")
    delete_parser.add_argument("index")
    subparsers.add_parser("total", help="Show total amount spent")
    subparsers.add_parser("menu", help="Open the interactive terminal menu")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        try:
            expense = add_expense(args.name, args.amount)
            print(f"Added: {expense['name']} - ${expense['amount']:.2f}")
        except ValueError as exc:
            print(f"Error: {exc}")
        return

    if args.command == "list":
        list_expenses()
        return

    if args.command == "delete":
        try:
            removed = delete_expense(args.index)
            print(f"Deleted: {removed['name']} - ${float(removed['amount']):.2f}")
        except (ValueError, IndexError) as exc:
            print(f"Error: {exc}")
        return

    if args.command == "total":
        show_total()
        return

    if args.command == "menu":
        interactive_menu()
        return

    interactive_menu()


if __name__ == "__main__":
    main()
