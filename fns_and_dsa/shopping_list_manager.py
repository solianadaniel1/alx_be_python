#!/usr/bin/python3

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("enter item to add")
            shopping_list.append(item)
            print(f"Added '{item}' to shopping list")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("enter '{item} to be removed'")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"the item '{item}' has been removed'")
            else:
                print("item not in the list")
            pass
        elif choice == '3':
            # Display the shopping list
            print("the shopping list", shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
