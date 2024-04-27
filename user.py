from income import Income
from expense import Expense
from savings import Savings
import pandas as pd


def main():
    username = input("Enter your username: ")
    month_year = input("Enter month and year (MM-YYYY): ")

    while True:
        finance_category = input(
            "Enter finance category (Income, Expense, Saving): ")

        if finance_category.lower() == 'income':
            income_module(username, month_year)
        elif finance_category.lower() == 'expense':
            expense_module(username, month_year)
        elif finance_category.lower() == 'saving':
            savings_module(username, month_year)
        else:
            print(
                "Invalid finance category. Please choose from Income, Expense, or Saving.")

        continue_input = input(
            "Do you want to continue inputting finances for the same month? (yes/no): ")
        if continue_input.lower() != 'yes':
            change_month = input(
                "Do you want to input for a different month? (yes/no): ")
            if change_month.lower() == 'yes':
                month_year = input("Enter month and year (MM-YYYY): ")
            else:
                break
  

def income_module(username, month_year):
    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))
    income = Income(source, amount)
    save_to_excel(username, month_year, "Income", source, amount)


def expense_module(username, month_year):
    expense_name = input("Enter expense name: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expense = Expense(expense_name, category, amount)
    save_to_excel(username, month_year, "Expense", category, amount)


def savings_module(username, month_year):
    saving_type = input("Enter saving type: ")
    amount = float(input("Enter saving amount: "))
    savings = Savings(saving_type, amount)
    save_to_excel(username, month_year, "Saving", saving_type, amount)


def save_to_excel(username, month_year, finance_category, category_type, amount):
    data = {'Username': username,
            'Month-Year': month_year,
            'Finance Category': finance_category,
            'Category Type': category_type,
            'Amount': amount}
    df = pd.DataFrame(data, index=[0])

    # Check if the file exists
    try:
        existing_data = pd.read_excel('finance_tracker.xlsx')
        updated_data = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        updated_data = df

    with pd.ExcelWriter('finance_tracker.xlsx', mode='a', if_sheet_exists='replace') as writer:
        updated_data.to_excel(writer, sheet_name='Sheet1', index=False)

if __name__ == "__main__":
    main()
