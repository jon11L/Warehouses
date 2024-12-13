from CLI.data import stock, personnel
import random

# YOUR CODE STARTS HERE
# user_name: str = None
list_of_operations: list = []
is_authenticated = False

# ------- functions here first :  -------------
# def decorator(func):
#     ''' decorator function to decor queries of user.'''
#     def inner(*args, **kwargs):
#         print('\n', '*' * 50, '\n')
#         func(*args, **kwargs)
#         print('\n', '*' * 50, '\n')
#     return inner


# try for username/password check decorator function
def find_personnel(user_name, password, personnel_list):

    for personnel_sub_list in personnel_list:
        # print(f"list of personnels are {personnel_sub_list}\n")
        if personnel_sub_list['user_name'] == user_name and personnel_sub_list['password'] == password:
            return True
        
        if 'head_of' in personnel_sub_list:
            if find_personnel(user_name, password, personnel_sub_list['head_of']):
                return True
    return False


def credential_validator(func):
    ''' decorator function to check credential of user.'''
    def inner(*args, **kwargs):
        global is_authenticated
        global user_name

        if is_authenticated:
            return func(*args, **kwargs)

        # password: str = None

        while not is_authenticated:
            print("*Only authenticated personnel can order in the warehouse.*\n")
            print(f"Current user: {user_name}.")

            password = input("Enter your password: ")
            print('\n', '*' * 20, '\n')
            print("Checking credientials...")


        # check with find_personel if credentials match one of the personel, return True if correct and False otherwise.
            if find_personnel(user_name, password, personnel):
                is_authenticated = True
                print(f"\n**Login successful.**\n Authenticated user: {user_name}\n")
                return func(*args, **kwargs)

            print("\n**Invalid credential**.",
                  f"\nuser-name and password could not be matched for User: '{user_name}' - Pw: '{password}'."
                  )

            new_choice = input("\nType (y) to retry, (c) to change the username and (q) to quit: ").lower()
            if new_choice in ['c', 'change']:
                user_name = input('\nType your username: ').capitalize()

            elif new_choice in ['q', 'quit']:
                new_operation()
                return None
            elif new_choice in ['y', 'yes']:
                continue

    return inner
# try to improve fucntion by finding if username is part of personnel[username] but no corresponding password
      
                # return None

            # for credential in personnel:
            #     print(f"list of credentials are {credential}\n")
            # # check if username/password is correct
            #     if user_name == credential['user_name'] and password == credential['password']:
            #         print("Valid credential. -->")
            #         is_authenticated = True
                
            #     elif user_name == credential['user_name'] and password != credential['password']:
            #         print("Invalid password. Please try again.")


def get_username():
    '''Get the user name.'''
    global user_name
    user_name = input('What is your user name? ').capitalize()
    return user_name


def greet_user(user_name):
    '''Greet the user.'''
    print(f"\nHello {user_name}, welcome.")
    return user_name


def menu(user_name):
    ''' Show the menu and ask to pick a choice '''
    print('\nWhat would you like to do?',
          '\n', '1. List items by warehouse.',
          '\n', '2. Search an item and place an order.',
          '\n', '3. browse by category.',
          '\n', '4. Quit. \n')
    menu_choice: int = None
    while not isinstance(menu_choice, int):
        try:
            menu_choice: int = int(input('Type the number of the operation: '))
        except ValueError:
            print("\n", "*"*30)
            print("Invalid input. Please enter a valid Number.")
            print("*"*30, "\n")

    # If they pick 1 and just check the list of items.
    if menu_choice == 1:
        list_item_by_warehouse()
    # if they pick 2 and user want to look for an item.
    elif menu_choice == 2:
        search_item(user_name)
    elif menu_choice == 3:
        browse_by_category()
    elif menu_choice == 4:
        exit(user_name)
    else:
        # when user did not pick unavailable option
        print("\n", "*"*30)
        print("Invalid choice. Please choose from the following option: 1-2-3-4.")
        print("*"*30, "\n")
        menu(user_name)

# @decorator
def new_operation():
    ''' ask the user if they want to make another operation,
    yes -> back to main menu, no -> exit
    '''
    new_op = False
    while new_op == False:
        new_operation_choice = input("\nWould you like to perform another operation? (y/n): ")
        if new_operation_choice.lower() in ['y', 'yes']:
            new_op = True
            return menu(user_name)
        elif new_operation_choice.lower() in ['n', 'no']:
            new_op = True
            return exit(user_name)



def list_item_by_warehouse():
    '''This function list items by warehouse.'''

    print("\nTo enter a warehouse, type it's corresponding number ex: '1' for Warehouse N.1 etc.. (up to 4 warehouses at the moment.)",
        "\n\n  - To view items from all the warehouses available simply press 'Enter/<Return>'.",
        "\n  - Type 'q' to go back to the main menu\n"
        )
    
    warehouse_choice = input("Please type here Warehouse choice: ").strip().lower()

    # if user press 'q' then back to the menu:
    if warehouse_choice == 'q':
        print("Back to main menu.")
        print("\n\n", "*"*30)
        return menu(user_name)
    
    # simply press Enter/Return:  select all warehouses, sort them by warehouse order.
    elif warehouse_choice == "": 
        list_stock_item = sorted(stock, key=lambda item: item['warehouse'], reverse=False)
        print(f"\nstock of all warehouses:\n\n")
        for num_item, list in enumerate(list_stock_item[800:840], start=1): # sample of 40 to showcase
            if num_item < 10:
                print(f"0{num_item}. {list}")
            else:
                print(f"{num_item}. {list}")

        # add to the list of operations: user checked items from all warehouses
        save_query = f"you have listed {len(list_stock_item)} items from all the warehouses."
        list_of_operations.append(save_query)
        
        return new_operation()


    elif warehouse_choice.isdigit():
        list_stock_item = [item for item in stock if item['warehouse'] == int(warehouse_choice)]
        print(f"\nProducts of Warehouse-{warehouse_choice}:\n")
        for num_item, list in enumerate(list_stock_item[100:130]): # sample of 30 to showcase
            num_item += 1 # use for numerate the items displayed
            if num_item < 10:
                print(f"0{num_item}. {list}")
            else:
                print(f"{num_item}. {list}")

        # if user selected non existent warehouse, does not add to the operation list
        if len(list_stock_item) == 0 or int(warehouse_choice) <= 0:
            print("it doesn't looks like this warehouse exists yet.\n")

        # add to the list of operations: user checked items from a specific warehouse.
        else:
            save_query = f"you have listed {len(list_stock_item)} items from warehouse {warehouse_choice}."
            list_of_operations.append(save_query)
        
        return new_operation()
    
    else:
        print("\n\n", "*"*30, "\nInvalid input. Please enter a number or press 'Enter' to view all warehouses.\n\n", "*"*30)
        
        return list_item_by_warehouse()




# @decorator
def search_item(user_name):
    ''' search an item through the stock warehouses. 
    If item found, returns to User the availability of this item and propose ordering.
    '''

    item_searched : str = ""
    while len(item_searched) == 0:
        item_searched = input(f"\nEnter the name of the item you are looking for. -- Type 'q' to go back to the main menu: ").capitalize()

    # if user press 'q' then back to the menu:
    if item_searched == 'q':
        return menu(user_name)


    # list_products_searched added to record of operations performed
    save_query = f"You searched for '{item_searched}'."
    list_of_operations.append(save_query)

    num = 0 # numbers individually each items in the warehouses globally
    list_item_searched = [] # will hold the list of items searched.

    for item in stock[:1500]: # only sample over part of the stock
        num += 1 
        # user search item through all warehouses.
        if item_searched == item['category']:
            list_item_searched.append(item)
            print(f"product {num}: {item}\n")

    # If no items are found, display this message.
    if len(list_item_searched) == 0:
        print(F"'{item_searched}' product not found in any warehouses.")
        new_operation()
    else:
        # display the amount of item found.
        print(f"There is {len(list_item_searched)} items available for '{item_searched}'.\n\n")

    user_order = None
    while user_order not in ['y', 'yes', 'no', 'n']:
        user_order = input(f"Would you like to order this item: '{item_searched}'?(y/n).  ").lower()
        if user_order in ['y', 'yes']:
            return ordering(list_item_searched, item_searched)

        elif user_order.lower() in ['n', 'no']:
            return new_operation()
            # break
        else:
            print('Invalid choice. Please choose from the option: y or n.')
            


@credential_validator
def ordering(list_item_searched: list, item_searched: str ):
    ''' function to order available products'''

    order_process = False
    while order_process == False:
        item_order_qty: int = None

        while item_order_qty == None:

            try:
                item_order_qty = int(input('how many would you like to order?  '))
            except ValueError:
                print(f"Invalid entry, please type only a valid number")

        if item_order_qty > len(list_item_searched):
            print('           ', '*'*50)
            print(f"\nThere are not this many products available for this item. The maximum amount that can be ordered is {len(list_item_searched)}.\n")
            print('           ', '*'*50)
            max_order = input('Do you want to order the maximum available amount? (y/n). ').lower()

            if max_order in ['y', 'yes']:
                print(f"You have successfully ordered the maximum available amount of: {len(list_item_searched)} {item_searched}s.\n")
                order_process = True
            else:
                pass

        elif item_order_qty == 0: # cancel the order
            print('you have not ordered anything / Cancelled')
            order_process = True

        elif item_order_qty == 1:
            print(f"you have successfully ordered {item_order_qty} '{item_searched}': {random.choice(list_item_searched)}.\n")
            order_process = True

        else: # user ordered several items
            print(f"you have successfully ordered {item_order_qty} {item_searched}s: {random.choice(list_item_searched)}.\n")
            order_process = True

        if order_process == True and item_order_qty != 0:
            list_of_operations.pop(-1)
            save_query = f"you ordered {item_order_qty} {item_searched}."
            list_of_operations.append(save_query)

    return new_operation()




def browse_by_category():
    ''' user can browse the stock warehouse by category'''

    # item_searched = None
    item_searched = input("Type the product category you want to browse: ").capitalize()
    print(f"\nHere are the available products for the category {item_searched}:\n")

    category_list = []
    for item in stock[:1000]: # sample over part of the stock
        if item_searched == item['category'] or item_searched == item['state']:
            category_list.append(item)
            browse_searched = f"{item['state']} {item['category']}  --  found in warehouse-{item['warehouse']} - in stock since: {item['date_of_stock']}\n"
            print(browse_searched)
    
    # if category found, then is added to the list of user's operation during the session
    if len(category_list) > 0:
        save_op = f"Browsed the category {item_searched}."
        list_of_operations.append(save_op)
    else:
        print(f"'{item_searched}' category not found in any warehouses.\n")


    return new_operation()



def exit(user_name):
    '''End of operations. And display list of actions made by user.'''

    global list_of_operations

    if len(list_of_operations) == 0:
        list_of_operations = "You have not performed any operations."
    else:
        num = 0
        for operation in list_of_operations:
            num += 1
            print(f"\n  {num}. {operation}")
    print(f"\nThank you for using our inventory management system.\n\nGoodbye {user_name}!\n")


def main():
    user_name = get_username()
    greet_user(user_name)
    menu(user_name)


if __name__ == "__main__":
    main()
    # user_name = get_username()
    # greet_user(user_name)
    # menu(user_name)

# state : new, red Original, Second hand, Brand new, White,  .... to copy when ran
