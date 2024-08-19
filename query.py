from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name
user_name = input('What is your username?: ').capitalize()

# Greet the user
print(f"Hello, {user_name}. \n")

# Show the menu and ask to pick a choice
print("\n",'*'*50, "\n")
print('What would you like to do?',
        '\n', '1. List items by warehouse.',
        '\n', '2. Search an item and place an order.',
        '\n', '3. Quit. \n')
print("\n",'*'*50, "\n")

choice_menu = int(input('Type the number of the operation: '))

# If they pick 1
if choice_menu == 1:
    print("\n Items in Warehouse 1: \n")
    for item in warehouse1:
        print(f"- {item}")
    print("\n Items in Warehouse 2:\n ")
    for item in warehouse2:
        print(f"- {item}")

# Else, if they pick 2
elif choice_menu == 2:
    item_searched = input('\nPlease enter the name of the item you are looking for: ').capitalize()

    count_item_w1 = warehouse1.count(item_searched)
    count_item_w2 = warehouse2.count(item_searched)
    total_items = count_item_w1 + count_item_w2

    if total_items > 0:
        # checking where the selected product are available.
        if count_item_w1 > 0 and count_item_w2 > 0:
            print(f"\n' {item_searched} '  //  'location: both Warehouses.\n")
            print(f"Amount available: {total_items}.")
            if count_item_w1 > count_item_w2:
                print(f"Warehouse 1 has the highest amount of this item, {count_item_w1} units in stock.\n")
            else:
                print(f"Warehouse 2 has the highest amount of this item, {count_item_w2} units in stock.\n")
        elif count_item_w1 > 0 and count_item_w2 == 0:
            print(f"' {item_searched} '\n 'location: Warehouse1.")
            print(f"{count_item_w1} units of this item were found.")
        elif count_item_w1 == 0 and count_item_w2 > 0:
            print(f"' {item_searched} '\n 'location: Warehouse2.")
            print(f"{count_item_w2} units of this item were found.")
        
        # prompting the user to order.
        user_order = input("Would you like to order this item? (y/n): ").lower()
        if user_order in ['y', 'yes']:
            number_item_order = int(input('how many would you like to order? '))
            if number_item_order > total_items:
                print("\n",'*'*50, "\n")
                print(f"There are not this many units available for this item. The maximum amount that can be ordered is {total_items}.")
                print("\n",'*'*50, "\n")
                order_max = input('Do you want to order the maximum available amount? (y/n). ').lower()
                if order_max in ['y', 'yes']:
                    print("\n",'*'*50, "\n")
                    print("\nOrder confirmed.\n")
                    print(f"order: \nitem: {item_searched}    Qty: {total_items}")
                else:
                    pass
            elif number_item_order == 0:
                print('you have not ordered anything')
            elif number_item_order == 1:
                print("\n",'*'*50, "\n")
                print("Order confirmed. \n")
                print(f"order: \nitem: {item_searched}    Qty: {number_item_order}")
                print("\n",'*'*50, "\n")
            else:
                print("\n",'*'*50, "\n")
                print("Order confirmed. \n")
                print(f"order: \nitem: {item_searched}    Qty: {number_item_order}")
                print("\n",'*'*50, "\n")
        elif user_order in ['n', 'no']:
            pass
        else:
            print("Invalid choice. please select Y for yes or any other key for no and exit.")
    else:
        print(f"'{item_searched}' item not in stock.")

# Else, if they pick 3
elif choice_menu == 3:
    pass

# when user did not pick unavailable option
else:
    print("\n",'*'*50, "\n")
    print('Invalid choice. Please choose from the option: 1, 2, or 3.')
    print("\n",'*'*50, "\n")

# Thank the user for the visit
print(f"\nThank you for your visit, {user_name} !\n")
