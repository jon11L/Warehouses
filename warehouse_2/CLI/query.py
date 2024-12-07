# Warehouse project :

"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock




# YOUR CODE STARTS HERE

# ------- functions here first :  -------------
def decorator(func):
    ''' decorator function to decor queries of user.'''
    def inner(*args, **kwargs):
        print('*' * 50, '\n')
        func(*args, **kwargs)
        print('\n', '*' * 50, '\n')
    return inner


@decorator
def menu():
    ''' Show the menu and ask to pick a choice '''
    print('What would you like to do?',
          '\n', '1. List items by warehouse.',
          '\n', '2. Search an item and place an order.',
          '\n', '3. Quit. ')


def search_item():
    item_searched = input('Please enter the name of the item you are looking for: ').capitalize()

    count_item_w1 = warehouse1.count(item_searched)
    count_item_w2 = warehouse2.count(item_searched)
    total_items = count_item_w1 + count_item_w2
    # print(f"amount available: {total_items}.")

    # checking where the wanted items are available.
    if count_item_w1 > 0 and count_item_w2 > 0:
        print(f"'{item_searched}'\n 'location: both Warehouses.")
        print(f"There is in total {total_items} products of this item available: ")

        if count_item_w1 > count_item_w2:
            print(f"warehouse 1 has the highest amount of this item, {count_item_w1} products in stock.")
        else:
            print(f"warehouse 2 has the highest amount of this item, {count_item_w2} products in stock.")
        ordering(total_items, item_searched)

    elif count_item_w1 > 0 and count_item_w2 == 0:
        print(f"'{item_searched}'\n 'location: Warehouse1.")
        print(f"{count_item_w1} products of this item were found.")
        ordering(total_items, item_searched)
    elif count_item_w1 == 0 and count_item_w2 > 0:
        print(f"'{item_searched}'\n 'location: Warehouse2.")
        print(f"{count_item_w2} products of this item were found.")
        ordering(total_items, item_searched)
    else:
        print(f"'{item_searched}' item not in stock.")

    return total_items, item_searched


def ordering(total_items, item_searched):
    ''' function to order item when available'''
    user_order = input("Would you like to order this item?(y/n).")
    if user_order in ['y', 'yes']:
        number_item_order = int(input('how many would you like to order? '))

        if number_item_order > total_items:
            print('*'*50)
            print(f"There are not this many products available for this item. The maximum amount that can be ordered is {total_items}.")
            print('*'*50)
            order_max = input('Do you want to order the maximum available amount? (y/n). ').lower()
            if order_max in ['y', 'yes']:
                print(f"You have successfully ordered the maximum available amount of: {total_items} {item_searched}s.")
            else:
                pass
        elif number_item_order == 0:
            print('you have not ordered anything')
        elif number_item_order == 1:
            print(f"you have successfully ordered {number_item_order} {item_searched}.")
        else:
            print(f"you have successfully ordered {number_item_order} {item_searched}s.")

    elif user_order.lower() == "n":
        pass
    else:
        print("Invalid choice. please select Y for yes or any other key for no and exit.")
    menu()


# --------    queries starts here. ----------

# Get the user name.
user_name = input('What is your user name?: ').capitalize()
# Greet the user.
print(f"Hello, {user_name}.")

# Show the menu and ask to pick a choice.
menu()
choice_menu = int(input('Type the number of the operation: '))

# If they pick 1 and just check the list of items.
if choice_menu == 1:
    print("\n Items in Warehouse 1: \n")
    for item in warehouse1:
        print(item)
    print("\n Items in Warehouse 2:\n ")
    for item in warehouse2:
        print(item)

# if they pick 2 and user want to look for an item.
elif choice_menu == 2:
    search_item()

# if user pick 3 and leave.
elif choice_menu == 3:
    print('Goodbye!')

# when user did not pick unavailable option
else:
    print('*'*50)
    print('Invalid choice. Please choose from the option: 1, 2, or 3.')
    print('*'*50)

# end!
print(f"\n Thank you for your visit, {user_name} !\n")



