from predefined_values import *


def int_input(message):
    while True:
        num = input(message)
        error = False
        for i in range(len(num)):
            if num[i] == "-":
                if i != 0:
                    error = True
                    break
            elif not (ord("0") <= ord(num[i]) and ord(num[i]) <= ord("9")):
                error = True
                break
            
        if error:
            print("Invalid Input. Please input a valid integer")
        else:
            return int(num)


def get_flavour_price(selected_flavour_index):
    return flavour_prices[selected_flavour_index]


def calculate_total_flavour_price(selected_icecream):
    selected_icecream_flavour_indices = combo_flavours[selected_icecream]
    total_flavour_price = 0
    
    for each_price in selected_icecream_flavour_indices:
        total_flavour_price = total_flavour_price + get_flavour_price(each_price)
        
    return total_flavour_price


def get_topping_price(selected_topping_index):
    return topping_prices[selected_topping_index]


def calculate_total_topping_price(selected_icecream):
    selected_icecream_topping_indices = combo_toppings[selected_icecream]
    total_topping_price = 0
    
    for each_price in selected_icecream_topping_indices:
        total_topping_price = total_topping_price + get_topping_price(each_price)
        
    return total_topping_price


def calculate_total_icecream_unit_price(selected_icecream):
    total_flavour_prices = calculate_total_flavour_price(selected_icecream)
    total_topping_price = calculate_total_topping_price(selected_icecream)
    
    return total_flavour_prices + total_topping_price


def get_icecream_name(selected_icecream):
    if selected_icecream == -1:
        return "Custom Ice cream"
    else:
        return list_combos[selected_icecream]


def get_flavour_name(flavour_index):
    return list_flavours[flavour_index]


def get_topping_name(topping_index):
    return list_toppings[topping_index]


def display_flavours_list():
    for i in range(len(list_flavours)):
        print(str(i + 1) + ". " + list_flavours[i])
        

def display_toppings_list():
    for i in range(len(list_toppings)):
        print(str(i + 1) + ". " + list_toppings[i])


def display_icecream_info(selected_item, shopping_cart_index=-1):
    if selected_item == -1:
        selected_icecream_name = "Custom Ice Cream"
        selected_icecream_flavours = chosen_flavours[shopping_cart_index]
        selected_icecream_toppings = chosen_toppings[shopping_cart_index]
    else:
        selected_icecream_name = list_combos[selected_item]
        selected_icecream_flavours = combo_flavours[selected_item]
        selected_icecream_toppings = combo_toppings[selected_item]
        
    print("Ice Cream Name: " + selected_icecream_name)
    print("Flavours:")
    
    total_price = 0
    
    for each_flavour_index in selected_icecream_flavours:
        print("- " + get_flavour_name(each_flavour_index))
        
        total_price = total_price + get_flavour_price(each_flavour_index)
        
    
    if len(selected_icecream_toppings) > 0:  # if there are any toppings at all
        print("Toppings:")
        
        for each_topping_index in selected_icecream_toppings:
            print("- " + get_topping_name(each_topping_index))
            
            total_price = total_price + get_topping_price(each_topping_index)
        
    print("Unit Price: " + str(total_price) + " " + CURRENCY_NAME)
    
    
def tabulated_display(column_headers, values):
    # column_headers: 1D list of strings
    # values: 2D list of any data type
    
    max_column_width = 0
    
    for each_column_header in column_headers:
        if len(each_column_header) > max_column_width:
            max_column_width = len(each_column_header)
            
    for each_row in values:
        for each_col in each_row:
            if len(str(each_col)) > max_column_width:
                max_column_width = len(str(each_col))
    
    
    # Add 2 extra spaces
    max_column_width = max_column_width + 2
                
    current_line = ""
    
    for each_column_header in column_headers:
        current_line = current_line + each_column_header
        
        for i in range(max_column_width - len(each_column_header)):
            current_line = current_line + " "
            
        current_line = current_line + "| "
        
    print(current_line)
    
    for each_row in values:
        current_line = ""
        
        for each_column in each_row:
            current_line = current_line + str(each_column)
            
            for i in range(max_column_width - len(str(each_column))):
                current_line = current_line + " "
            
            current_line = current_line + "| "
        
        print(current_line)


def to_lower(string):
    output = ""
    
    for each_char in string:
        if (ord("A") <= ord(each_char)) and (ord(each_char) <= ord("Z")):
            output = output + chr(ord("a") + (ord(each_char) - ord("A")))
        else:
            output = output + each_char
            
    return output
