expenses = []
def add_expense(name, price):
    expenses.append({"item" :name, "cost":price})
    print(f"Added {name} for ${price}")
def view_expense():
    total = 0
    print("\n    Your Expense Report  ")
    for expense in expenses:
        total += expense["cost"]
        print(f"{expense['item']} : ${expense['cost']}")
    print(f"Total Expenses: ${total}")       
    print("              \n")

while True:
        print("1. Add\n2. View All & Total\n3. Exit")
        choice = input("Enter a choice = ")
        if choice == "1":
             item_name = input("What did you buy? ")
             try:
                  item_cost = float(input("How much did it cost? "))
                  add_expense(item_name , item_cost)
             except ValueError:
              print("Invalid price! Please enter a number.")
        elif choice == "2":
            if not expenses:
                print("Your list is empty!")
            else:
                view_expense()
        elif choice == "3":
            print ("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")




