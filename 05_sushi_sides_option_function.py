# STRING CHECKER FUNCTION

def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

# MAIN MENU SUSHI PRICE CALCULATION


def calc_sushi_price(var_sushi):
    price = 0
    if var_sushi == "salmon":
        price = 10

    elif var_sushi == "teriyaki":
        price = 12

    elif var_sushi == "california":
        price = 12

    elif var_sushi == "vegan":
        price = 8

    return price


sushi_cost = calc_sushi_price


# MAIN ROUTINE FOR FUNCTIONS

temp_sides = []
which_sides = 'none'
yes_no_list = ["yes", "no"]
size_list = ["6pack", "8pack"]
side_list = ["miso", "tempura", "soy", "wasabi", "xxx"]

# SIDES FUNCTION

want_sides = string_checker("Would you like sides with your order? (y/n): ",
                            1, yes_no_list)


def sides():
    print('''\n

----- SIDES -----

Please select which sides you want by typing in the name from the list below:
Miso Soup (miso) $5.00
Shrimp Tempura (tempura) $2.00
Soy Sauce (soy) $0.50
Wasabi (wasabi) $0.50

-----------------------------------------------------------------------------''')


if want_sides == "yes":
    sides()
    while which_sides != 'xxx':
        which_sides = string_checker("Which sides would you like (type in \'xxx\' to quit): ",
                                     1, side_list)
        if which_sides == "miso":
            print("You selected Miso Soup as a side")
            sushi_cost = sushi_cost + 5
            temp_sides.append(which_sides)
            pass

        elif which_sides == "tempura":
            print("You selected Shrimp Tempura as a side")
            sushi_cost = sushi_cost + 2
            temp_sides.append(which_sides)
            pass

        elif which_sides == "soy":
            print("You selected Soy Sauce as a side")
            sushi_cost = sushi_cost + 0.5
            temp_sides.append(which_sides)
            pass

        elif which_sides == "wasabi":
            print("You selected Wasabi as a side")
            sushi_cost = sushi_cost + 0.5
            temp_sides.append(which_sides)
            pass

        elif which_sides == 'xxx':
            if len(temp_sides) > 0:
                print("No more sides to be added!")
            else:
                print("No Sides will be added then!")
                temp_sides.append("None")
    pass
