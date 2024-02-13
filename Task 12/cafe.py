#For this task, we need to create a list of items in a cafe menu, a dictionary of the price of each item,
#and a dictionary of the stock of each item. Once we have the list and two dictionaries, we need to calculate
#and print out the 'total_stock' worth in the cafe.
#Instead of having static variables when running the program, I will ask the user to enter each of the four items,
#adding each input to the correspondant list, key and value of the each dictionary. After that, the program will loop
#through each item in the price and stock dictionaries, using the item list, and print out 'total_stock'.

#Task does specify that the menu consists of 4 items; to expand the functionality of this code, I have created a
#custom function to ask the user for how many items they have in the menu. 'total_menu' variable is set to 4 as per
#task specifications, and I have commented out the part where it asks user for this input.

#=====================================================CODE=====================================================#

menu_item_list = []
item_price_dic = {}
item_stock_dic = {}
menu_item = ""
item_price = ""
item_stock = ""
total_stock = 0
total_menu = 4

class NegativeNumberException(Exception):
    def __init__(self, value_type, value):
        self.value_type = value_type
        self.value = value
        super().__init__(f"Error: {value} is not a valid entry. {value_type} should be a positive number")

def menu_range():
    while True:
        try:
            total_menu = int(input("\nFirst of all, how many items are there in your menu: "))
            if total_menu < 0:
                raise NegativeNumberException("Number of items in your menu", total_menu)
            
            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except NegativeNumberException as ne:
            print(ne)

    return total_menu

def construct_menu():
    while True:    
        try:
            menu_item = input("\nPlease enter the name of the item: ")
            if not menu_item.isalpha():
                raise ValueError("The name of the item must be a string")
            
            item_price = float(input("\nPlease enter the price of the item: "))
            if item_price < 0:
                raise NegativeNumberException("Price", item_price)
            
            item_stock = int(input("\nPlease enter the available stock of the item: "))
            if item_stock <0:
                raise NegativeNumberException("Stock", item_stock)
            
            break
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except NegativeNumberException as ne:
            print(ne)

    return menu_item, item_price, item_stock

print("""Welcome to the 'Menu Calculator'! With this tool, you will enter the name, price and stock
of your menu; after that, the calculator will return the total value of the menu""")

#while True:
#    total_menu = menu_range()
#    break

for entry in range(total_menu):
    menu_item, item_price, item_stock = construct_menu()
    menu_item_list.append(menu_item)
    item_price_dic[menu_item] = item_price
    item_stock_dic[menu_item] = item_stock

for items in (menu_item_list):
    total_stock += item_price_dic[items]*item_stock_dic[items]

print(f"\nThe total value of your menu is {total_stock}")