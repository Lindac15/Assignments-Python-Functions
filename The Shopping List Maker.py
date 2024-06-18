#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a feature to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list = ['rice', 'beans']

def manage_list():
    while True:
        print("What would you like to do to your grocery list?")
        print("1. View or Print the items in your shopping list")
        print("2. Add an item from your shopping list")
        print("3. Remove an item to from shopping list")
        print("4. Done editing your shopping list")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Here is your shopping list:")
            for i, item in enumerate (shopping_list):
                print(f' Item {i}: {item}') 
        elif choice == "2":
            new_item = input("What item would you like to add? ") 
            shopping_list.append(new_item)
            print(new_item + " has been added to your shopping list.")
        elif choice == "3": 
            remove_item = input("What item would you like to remove? ")
            if item in shopping_list:
                shopping_list.remove(remove_item)
                print(remove_item + " has been removed from your shopping list.")
            else:
                print(remove_item + " is not in your shopping list.")
        elif choice == "4":
            print("Thank you for using the shopping list maker. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

manage_list()









