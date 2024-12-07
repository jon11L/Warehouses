from data import stock


# def main():
#     print(
#         "What would you like to do?",
#         "\n",
#         "1. List items by warehouse",
#         "\n",
#         "2. Search an item and place an order",
#         "\n",
#         "3. Quit, ",
#     )

#     choice = int(input("Type the number of the operation: "))

#     # If they pick 1 and just check the list of items
#     if choice == 1:
#         print("\n", "Warehouse 1:", "\n", "\n", warehouse1)
#         print("\n", "warehouse 2:", "\n", "\n", warehouse2)

#     # Else, if they pick 2 and user want to look for an item.
#     elif choice == 2:
#         item_wanted = input("Please enter the name of the item you are looking for: ")
#         count1_item = 0
#         count2_item = 0

#         for item in warehouse1:
#             if item_wanted in item:
#                 count1_item += 1

#         for item in warehouse2:
#             if item_wanted in item:
#                 count2_item += 1

#         total_count = count1_item + count2_item

#         # checking where the wanted items are available.
#         if count1_item > 0 and count2_item > 0:
#             print(
#                 '"',
#                 item_wanted,
#                 '"',
#                 "\n",
#                 "location : item is available in both Warehouses",
#             )
#             print("There is in total", total_count, "product of this item available: ")

#             if count1_item > count2_item:
#                 print(
#                     "warehouse 1 has the highest amount of this item with",
#                     count1_item,
#                     "products in stock",
#                 )
#             else:
#                 print(
#                     "warehouse 2 has the highest amount of this item",
#                     count2_item,
#                     "products in stock",
#                 )
#             ordering()

#         elif count1_item > 0 and count2_item == 0:
#             print(
#                 '"',
#                 item_wanted,
#                 '"',
#                 "\n",
#                 "location: item only available in Warehouse1",
#             )
#             print(count1_item, "products of this item were found")
#             ordering()
#         elif count1_item == 0 and count2_item > 0:
#             print(
#                 '"',
#                 item_wanted,
#                 '"',
#                 "\n",
#                 "location: item only available in Warehouse2",
#             )
#             print(count2_item, "products of this item were found")
#             ordering()
#         else:
#             print('"', item_wanted, '"', " item not in stock")

#     # if user pick 3 and leave.
#     elif choice == 3:
#         print("Goodbye!")
#         # break

#     # when user did not pick unavailable option
#     else:
#         print("Invalid choice. Please choose 1, 2, or 3.")


# main()


warehouse1 = []
for item in stock:
    if item['warehouse'] == 1:
        warehouse1.append(item)
        item_almost_new = []
        for sub_item in item:
            if sub_item['state'] == "Almost new":
                item_almost_new.append(sub_item)
                print(item_almost_new)
