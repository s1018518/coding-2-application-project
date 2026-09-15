employees = []

projects = {}

# TODO: Add a new item to the store
def add_project(food, price, quantity):
  projects[food] = {}
  projects[food]["price"] = price
  projects[food]["quantity"] = quantity
  print("\nItem added!\n")

# TODO: Display the items in the store
def view_store():
  if len(projects) == 0:
    print("\nThere is nothing in your projects.\n")
  else:
    print("\nStore:\n")
    for item in projects:
      print(item + ", $" + str(projects[item]["price"]) + ", Quantity " + str(projects[item]["quantity"]) + "\n")

# TODO: Find an item in the store and return its information
def find_item(food):
  if food in projects:
    print("\n" + item + ", $" + str(projects[item]["price"]) + ", Quantity " + str(projects[item]["quantity"]) + "\n")
  else:
    print("\nThat item is not in your projects.\n")

# TODO: Change the quantity of an item
def update_quantity(food, quantity):
  projects[food]['quantity'] = quantity
  print("\nUpdated the quantity.\n")

# TODO: Remove an item from the store
def remove_item(food):
    pass

# TODO: Calculate the total and update the store
def checkout(cart):
    pass


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("\n" + "=" * 40)
    print("           Project Management")
    print("=" * 40)

    print("1. Add Project")
    print("2. View Projects")
    print("3. Find Projects")
    print("4. Update Projects")
    print("5. Remove Projects")
    print("6. Add Employee")
    print("7. Quit")

    choice = input("\nWhat would you like to do? ").strip()

    if choice == "1":
      item = input("\nWhich item would you like to add? ")
      if item in foods:
        try:
          quantity = int(input("\nHow many do you want (No decimals)? "))
          add_item(item, prices[foods.index(item)], quantity)
        except ValueError:
          print("\nThat is not a correct value.")
          
      else:
        print("\nThat is not an item in the projects.\n")

    elif choice == "2":
      view_store()

    elif choice == "3":
      item = input("\nWhich item do you want to search for? ")
      find_item(item)

    elif choice == "4":
      item = input("\nWhich item would you like to update? ")
      if item in projects:
        try:
          quantity = int(input("\nHow many do you want (No decimals)? "))
          update_quantity(item, quantity)
        except ValueError:
          print("\nThat is not a correct value.")
      else:
        print("\nThat is not an item in your projects.\n")

    elif choice == "5":
      item = input("\nWhich item would you like to remove? ")
      if item in projects:
      else:
        print("\nThat is not an item in your projects.\n")
        pass

    elif choice == "6":
        pass

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please choose 1-7.")