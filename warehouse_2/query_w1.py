from CLI.data import stock


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
          '\n', '3. browse by category.',
          '\n', '4. Quit. \n')

    choice_menu = int(input('Type the number of the operation: '))


    # If they pick 1 and just check the list of items.
    if choice_menu == 1:
        list_item_by_warehouse()

    # if they pick 2 and user want to look for an item.
    elif choice_menu == 2:
        search_item()

    elif choice_menu == 3:
        # need to add a browse by category()
        pass

    # if user pick 3 and leave.
    elif choice_menu == 4:
        print(f'Goodbye! {user_name}')

    # when user did not pick unavailable option
    else:
        print('*'*50, "\n")
        print('Invalid choice. Please choose from the option: 1, 2, or 3.')
        print('*'*50, "\n")
        menu()







def list_item_by_warehouse():
    '''This function list items by warehouse.'''
    #  select all warehouses
    # print(stock)

    # print individual warehouse
    # trying to sort the warehouse with list methods
    sorted_warehouses = sorted(stock, key=lambda item: item['warehouse'], reverse=False)
    
    print(f"Sorted stock by warehouses: {sorted_warehouses[0:10]}\n")
    menu()
    return sorted_warehouses
    #------- to try to sort the dictionary by warehouse wihtout creating each warehouse+:
    # Sort the books by sales numbers in descending order
    # sorted_books = sorted(book_dict.items(), key=lambda x: x[1], reverse=True)


    # # create lists for each warehouse. 
    # warehouse_1 = [] #
    # warehouse_2 = [] #:  list | dict 
    # warehouse_3 = [] #:  list | dict
    # warehouse_4 = [] #:  list | dict

    # print(f"Warehouse 1:\n Item list:")
    # # sort the items by warehouses. can be edited to sort by state, category and date_of_stock
    # for item in stock[0:80]:
    #     if item['warehouse'] == 1:
    #         warehouse_1.append(item)

    #         # item_almost_new = []
    #         # for sub_item in item:
    #         #     if sub_item['state'] == "Almost new":
    #         #         item_almost_new.append(sub_item)
    #         #         print(item_almost_new)

    #     elif item['warehouse'] == 2:
    #         warehouse_2.append(item)
    #     elif item['warehouse'] == 3:
    #         warehouse_3.append(item)
    #     elif item['warehouse'] == 4:
    #         warehouse_4.append(item)

    # print(f"Warehouse 1 items: {warehouse_1}\n")
    # print(f"Warehouse 2 items: {warehouse_2}\n")
    # print(f"Warehouse 3 items: {warehouse_3}\n")
    # print(f"Warehouse 4 items: {warehouse_4}\n")
    # print(warehouse_1[0]['category'])
    








def search_item():
    print("\n")
    item_searched = input('Please enter the name of the item you are looking for: ').capitalize()

    print("Enter the warehouse number you want to check (ex: '1', for Warehouse N.1 etc..  For listing items from all  Warehouses available type '0'.)")
    warehouse_choice = input("Please type here Warehouse choice: ")

    num = 0
    item_number = 0
    
    # display items in warehouse from the dictionary key 'category'.
    # for item in stock[:1000]:
    #     num += 1
    #     category = item['category']
    #     if category == item_searched:
    #         item_number += 1
    #         print(f"{num}: {item}")
        

    list_products_searched = []
    for item in stock[:1000]:
        num += 1 
        if int(warehouse_choice) == 0 and item_searched == item['category']:
            item_number += 1
            print(f"product {num}: {item}\n")

        if int(warehouse_choice) == item['warehouse'] and item_searched == item['category']:
            item_number += 1
            print(f"product {num}: {item}\n")

    print(f"There is {item_number} items available for '{item_searched}'.\n\n")


# -------------------------------------------
    # try to display all products available after announcing how nmany there are available need to separate the list so that it display one per line.
    # list_products_searched.append(item)
    # list_items_searched = list_products_searched.split('\n')
    # print(f"Here are the prodcuts available:{item_number} {list_items_searched}\n")



    menu()


    # count_item_w1 = warehouse1.count(item_searched)
    # count_item_w2 = warehouse2.count(item_searched)
    # total_items = count_item_w1 + count_item_w2
    # # print(f"amount available: {total_items}.")

    # # checking where the wanted items are available.
    # if count_item_w1 > 0 and count_item_w2 > 0:
    #     print(f"' {item_searched} '\n 'location: both Warehouses.\n")
    #     print(f"There are a total of {total_items} units of this product available: ")

    #     if count_item_w1 > count_item_w2:
    #         print(f"warehouse 1 has the highest amount of this product, {count_item_w1} units in stock.")
    #     else:
    #         print(f"warehouse 2 has the highest amount of this product, {count_item_w2} units in stock.")
    #     ordering(total_items, item_searched)

    # elif count_item_w1 > 0 and count_item_w2 == 0:
    #     print(f"' {item_searched} '\n 'location: Warehouse1.")
    #     print(f"{count_item_w1} units of this product were found.")
    #     ordering(total_items, item_searched)
    # elif count_item_w1 == 0 and count_item_w2 > 0:
    #     print(f"' {item_searched} '\n 'location: Warehouse2.")
    #     print(f"{count_item_w2} units of this product were found.")
    #     ordering(total_items, item_searched)
    # else:
    #     print(f"'{item_searched}' product not in stock.")

    # return total_items, item_searched





def ordering(total_items, item_searched):
    ''' function to order available products'''
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
def get_username():
    user_name = input('What is your user name?: ').capitalize()
    return user_name

def greet_user(user_name):
    # Greet the user.
    print(f"Hello, {user_name}.")




# Show the menu and ask to pick a choice.
# menu()




# end!
# print(f"\n Thank you for your visit, {user_name} !\n")


if __name__ == "__main__":
    user_name = get_username()
    greet_user(user_name)
    menu()
    