from data import warehouse1, warehouse2


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
    choice_menu = int(input('Type the number of the operation: '))
    return choice_menu




def search_item():
    item_searched = input('Please enter the name of the item you are looking for: ').lower()
    item_W1 = [item for item in warehouse1 if item_searched in item.lower()]
    item_W2 = [item for item in warehouse2 if item_searched in item.lower()]
    print(item_W1)
    print(item_W2)
    # -- comprehension works to take element from the input into a new list.





# --------    queries starts here. ----------

# Get the user name.
user_name = input('What is your user name?: ').capitalize()
# Greet the user.
print(f"Hello, {user_name}.")

# Show the menu and ask to pick a choice.
menu()
# choice_menu = int(input('Type the number of the operation: '))

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
    print('*'*50, "\n")
    print('Invalid choice. Please choose from the option: 1, 2, or 3.')
    print('*'*50, "\n")
    menu()

# end!
print(f"\n Thank you for your visit, {user_name} !\n")





def search_item():
    item_searched = input('Please enter the name of the item you are looking for: ').capitalize()

    item_W1 = [item for item in warehouse1 if item_searched in item]
    print(item_W1)
    # -- comprehension works to take element from the input into a new list.
