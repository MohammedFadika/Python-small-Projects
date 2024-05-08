# Function to add a new expense
def add_expense(expenses, amount, category):
   expenses.append({'amount': amount, 'category': category})

# Function to print all expenses
def print_expenses(expenses):
   for expense in expenses:
       print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate total expenses
def total_expenses(expenses):
   return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
   return filter(lambda expense: expense['category'] == category, expenses)

def main():
   expenses = []  # Initialize expenses list

   while True:
       print('\nExpense Tracker')
       print('1. Add an expense')
       print('2. List all expenses')
       print('3. Show total expenses')
       print('4. Filter expenses by category')
       print('5. Exit')

       choice = input('Enter your choice: ')

       if choice == '1':
           # Add a new expense
           amount = float(input('Enter amount: '))
           category = input('Enter category: ')
           add_expense(expenses, amount, category)

       elif choice == '2':
           # List all expenses
           print('\nAll Expenses:')
           print_expenses(expenses)

       elif choice == '3':
           # Show total expenses
           print('\nTotal Expenses: ', total_expenses(expenses))

       elif choice == '4':
           # Filter expenses by category
           category = input('Enter category to filter: ')
           print(f'\nExpenses for {category}:')
           expenses_from_category = filter_expenses_by_category(expenses, category)
           print_expenses(expenses_from_category)

       elif choice == '5':
           # Exit the program
           print('Exiting the program.')
           break

if __name__ == '__main__':
   main()