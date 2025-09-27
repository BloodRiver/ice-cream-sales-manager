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


def create_custom_combo(update_index=-1):
    if update_index == -1:
        new_combo_flavours = []
        new_combo_toppings = []
    else:
        new_combo_flavours = chosen_flavours[update_index].copy()
        new_combo_toppings = chosen_toppings[update_index].copy()
    
    while True:
        print("1. Add Flavour")
        print("2. Remove Flavour")
        print("3. Add Topping")
        print("4. Remove Topping")
        print("5. Display Current Custom Combo Information")
        print("6. Add Custom Combo to Cart")
        print("7. Cancel and Go Back")
        
        choice = int_input("Enter your choice: ")
        
        if choice == 1:  # Add Flavour
            display_flavours_list()
            flavour_choice = int_input("Please choose a flavour to add: ") - 1
            
            if 0 <= flavour_choice and flavour_choice <= len(list_flavours):
                new_combo_flavours.append(flavour_choice)
            else:
                print("Invalid Input. Please choose between 1 and " + str(len(list_flavours)))
        elif choice == 2:  # Remove Flavour
            if len(new_combo_flavours) > 0:
                for i in range(len(new_combo_flavours)):
                    print(str(i + 1) + ". " + get_flavour_name(new_combo_flavours[i]))
                remove_flavour = int_input("Please choose a flavour to remove: ") - 1
                
                if 0 <= remove_flavour and remove_flavour <= len(new_combo_flavours):
                    new_combo_flavours.pop(remove_flavour)
                    print("Flavour removed.")
                else:
                    print("Invalid choice. Please enter a number between 1 and " + str(len(new_combo_flavours)))
            else:
                print("You have not added any flavours to the custom combo")
        elif choice == 3:  # Add Topping
            display_toppings_list()
            
            topping_choice = int_input("Please choose a topping to add: ") - 1
            
            if 0 <= topping_choice and topping_choice <= len(list_toppings):
                new_combo_toppings.append(topping_choice)
            else:
                print("Invalid Input. Please choose between 1 and " + str(len(list_toppings)))
        elif choice == 4:  # Remove Topping
            if len(new_combo_toppings) > 0:
                for i in range(len(new_combo_toppings)):
                    print(str(i + 1) + ". " + get_topping_name(new_combo_toppings[i]))
                remove_topping = int_input("Please choose a topping to remove: ") - 1
                
                if 0 <= remove_topping and remove_topping <= len(new_combo_toppings):
                    new_combo_toppings.pop(remove_topping)
                    print("Topping removed.")
                else:
                    print("Invalid choice. Please enter a number between 1 and " + str(len(new_combo_toppings)))
            else:
                print("You have not added any toppings to the custom combo")
        elif choice == 5:  # Display current custom combo information
            print("Flavours:")
            
            for each_flavour_index in new_combo_flavours:
                print("- " + get_flavour_name(each_flavour_index))
            
            print("Toppings:")
            
            for each_topping_index in new_combo_toppings:
                print("- " + get_topping_name(each_topping_index))
        elif choice == 6:  # Add current custom combo to cart
            if update_index == -1:
                chosen_icecreams.append(-1)
                chosen_flavours.append(new_combo_flavours)
                chosen_toppings.append(new_combo_toppings)
                print("Successfully added to cart!")
            else:
                chosen_icecreams[update_index] = -1
                chosen_flavours[update_index] = new_combo_flavours
                chosen_toppings[update_index] = new_combo_toppings
                print("Combo updated")
            break
        elif choice == 7:  # Go back
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")


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
                add_to_cart(selected_icecream - 1)
                print("Successfully added to cart!")
                break
            elif choice == 2:
                add_to_cart(selected_icecream - 1)
                create_custom_combo(len(chosen_icecreams)-1)
                break
            elif choice == 3:  # Go Back
                break
            else:
                print("Invalid input.")


def confirm_order():
    # Show tabulated prices
    column_headers = ["SL No.", "Ice Cream Name", "Unit Price"]
    
    values = []
    total_price = 0
    for i in range(len(chosen_icecreams)):
        price = calculate_total_icecream_unit_price(i)
        values.append([i + 1, get_icecream_name(chosen_icecreams[i]), price])
        total_price = total_price + price
        
    tabulated_display(column_headers, values)
    print("--------------------------------------")
    
    print("Total Price: " + str(total_price))
    
    confirmation = input("Are you sure you wish to confirm the order?(y/yes/n/no): ")
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
            if chosen_icecreams[choice - 1] == -1:
                display_icecream_info(chosen_icecreams[choice - 1], choice - 1)
            else:
                display_icecream_info(chosen_icecreams[choice - 1])
                
            while True:
                print("1. Customize Combo")
                print("2. Go Back")
                option = int_input("Enter your choice: ")
            
                if option == 1:
                    create_custom_combo(choice - 1)
                    break  
                elif option == 2:
                    break
                else:
                    print("Invalid Input. Please choose between 1 and 2.")
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
