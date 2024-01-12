def initialize_tracker(initial_balance):
    print("salary of arun in a month:",initial_balance)
    return {
        'balance':initial_balance,
        'expenses':[]
    }
def add_expense(tracker, amount, description):
    tracker['balance'] -= amount
    tracker['expenses'].append((amount, description))
def view_balance(tracker):
    return tracker['balance']
def view_expenses(tracker):
    return tracker['expenses']
def track_expenses():
    expense_tracker = initialize_tracker(50000)
    add_expense(expense_tracker,5500,"Groceries")
    add_expense(expense_tracker,3000,"Dinner")
    add_expense(expense_tracker,3500,"Travel")
    print("Current Balance:", view_balance(expense_tracker))
    print("Expenses:", view_expenses(expense_tracker))
track_expenses()