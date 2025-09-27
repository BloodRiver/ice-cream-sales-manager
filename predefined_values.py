list_flavours = ["Chocolate", "Vanilla", "Strawberry", "Butterscotch", "Ambrosia", "Mint"]
list_toppings = ["Oreos", "Chocolate Chips", "Chocolate Syrup", "Strawberry Syrup", "Almonds", "Cashew Nuts", "Pistacchio"]
list_combos = ["Chocolate Delight", "Oreo Fudge", "Neopolitan"]

combo_flavours = [
    [0],       # Chocolate Delight -> Chocolate (index 0 of list_flavours)
    [0, 1],    # Oreo Fudge -> Chocolate, Vanilla (index 0, 1)
    [0, 1, 2]  # Neopolitan -> Chocolate, Vanilla, Strawberry (index 0, 1, 2)
]

combo_toppings = [
    [1, 2],  # Chocolate Delight -> Chocolate Chips, Chocolate Syrup (index 1 and 2 of list_toppings)
    [0, 2],  # Oreo Fudge -> Oreos, Chocolate Syrup (index 0, 2)
    []
]

flavour_prices = [
    10,  # Chocolate
    10,  # Vanilla
    10,  # Strawberry
    20,  # Butterscotch
    25,  # Ambrosia
    15   # Mint
]

topping_prices = [
    25,  # Oreos
    10,  # Chocolate Chips
    15,  # Chocolate Syrup
    15,  # Strawberry Syrup
    5,   # Almonds
    5,   # Cashew Nuts
    5    # Pistacchio
]


CURRENCY_NAME = "Taka"


chosen_icecreams = []  # 1D list containing indices of existing combos or -1 for Custom Ice Cream
chosen_flavours = []  # 2D list containing indices of flavours for each chosen ice cream
chosen_toppings = []  # 2D list containing indices of toppings for each chosen ice cream
