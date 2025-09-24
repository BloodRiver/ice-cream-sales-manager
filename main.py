from utility_functions import *
from database_functions import *


def display_menu():
    print("1. Browse Ice Cream Combos")
    print("2. Create Custom Combo")
    print("3. View Shopping Cart")
    print("4. Exit")
    
    choice = int_input("Please enter your choice: ")
    
    return choice


def add_to_cart(selected_icecream):
    chosen_icecreams.append(selected_icecream)
    chosen_flavours.append(combo_flavours[selected_icecream])
    chosen_toppings.append(combo_toppings[selected_icecream])


def display_browse_combos_menu():
    list_combos = load_combos()
    
    for i in range(len(list_combos)):
        print(str(i + 1) + ". " + list_combos[i])
    
    print(str(i + 2) + ". " + "Go Back")
    
    choice = int_input("Please enter your choice: ")
    
    return choice

def browse_combos():
    selected_icecream = display_browse_combos_menu()
    
    if (0 < selected_icecream) and (selected_icecream < len(list_combos) + 1):
        display_icecream_info(selected_icecream - 1)
        
        while True:
            print("1. Add to Cart")
            print("2. Customize")
            print("3. Go Back")
            
            choice = int_input("Please enter your choice: ")
            
            if choice == 1:
                add_to_cart(selected_icecream)
                print("Successfully added to cart!")
                break
            elif choice == 2:
                pass
            elif choice == 3:  # Go Back
                break
            else:
                print("Invalid input.")


def create_custom_combo():
    print("1. Add Flavour")
    print("2. Remove Flavour")
    print("3. Add Topping")
    print("4. Remove Topping")
    print("5. Display Custom Combo Information")  # Tabulated display
    print("6. Add Custom Combo to Cart")
    print("7. Cancel and Go Back")


def confirm_order():
    # Show tabulated prices
    column_headers = ["SL No.", "Ice Cream Name", "Unit Price"]
    
    values = []
    
    for i in range(len(chosen_icecreams)):
        values.append([i + 1, get_icecream_name(chosen_icecreams[i]), calculate_total_icecream_unit_price(i)])
        
    tabulated_display(column_headers, values)
    print("--------------------------------------")
    
    confirmation = input("Are you sure you wish to confirm the order?")
    confirmation = to_lower(confirmation)
    
    
    # let user choose yes or no
    if confirmation == "y" or confirmation == "yes":
        save_order_to_database()
        print("Order Saved Successfully!")


def view_shopping_cart():
    while True:
        if len(chosen_icecreams) == 0:
            print("There are currently no items in the shopping cart")
            break

        for i in range(len(chosen_icecreams)):
            print(str(i + 1) + ". " + get_icecream_name(chosen_icecreams[i]))
        
        print(str(i + 2) + ". Confirm Order")
        print(str(i + 3) + ". Go Back")
        
        choice = int_input("Please enter your choice: ")
        
        if (0 < choice) and (choice <= len(chosen_icecreams)):
            display_icecream_info(choice - 1)
        elif (choice == i + 2):  # Confirm Order
            confirm_order()
            break
        elif choice == i + 3:  # Go Back
            break
        else:
            print("Invalid Input")


while True:
    selected_option = display_menu()
    
    if selected_option == 1:
        browse_combos()
    elif selected_option == 2:
        create_custom_combo()
    elif selected_option == 3:
        view_shopping_cart()
    elif selected_option == 4:  # Exit
        break
    else:
        print("Invalid Choice. Please choose between 1 and 3")
