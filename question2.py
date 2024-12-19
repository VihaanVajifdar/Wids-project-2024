import csv
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os

FILE_PATH="expenses.csv"
def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH,"r") as file:
            return csv.load(file)
    return []
def save_data(data):
    with open(FILE_PATH,"w") as file:
        csv.dump(data,file,indent=4)

def add_expense(date,category,amount,description=""):
    data=load_data()
    expense={
        "date":date,
        "category":category,
        "amount":amount,
        "description":description,
    }
    data.append(expense)
    save_data(data)

def edit_expense(index,date=None,category=None,amount=None,description=None):
    data=load_data()
    if 0<= index < len(data):
        if date: data[index]["date"]= date
        if category: data[index]["category"]= category
        if amount: data[index]["amount"]= amount
        if description: data[index]["description"]= description
        save_data(data)
    else:
        print("invalid index")

def delete_expense(index):
    data=load_data()
    if 0<= index < len(data):
        data.pop(index)
        save_data(data)
    else:
        print("invalid index.")


def total_spending(start_date=None, end_date=None):
    data = load_data()
    total = 0
    for expense in data:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if (not start_date or expense_date >= start_date) and (not end_date or expense_date <= end_date):
            total += expense["amount"]
    return total


def spending_by_category():
    data = load_data()
    category_totals = {}
    for expense in data:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    return category_totals

def highest_spending_category():
    breakdown = spending_by_category()
    if breakdown:
        return max(breakdown, key=breakdown.get)
    return None

# Pie chart for spending by category
def plot_spending_by_category():
    breakdown = spending_by_category()
    labels = list(breakdown.keys())
    sizes = list(breakdown.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.show()

def plot_monthly_trends():
    data = load_data()
    monthly_totals = {}
    for expense in data:
        month = expense["date"][:7]  # YYYY-MM format
        monthly_totals[month] = monthly_totals.get(month, 0) + expense["amount"]
    months = sorted(monthly_totals.keys())
    totals = [monthly_totals[month] for month in months]
    sns.lineplot(x=months, y=totals, marker="o")
    plt.xticks(rotation=45)
    plt.title("Monthly Spending Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.show()










































