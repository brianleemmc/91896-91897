# CURRENCY

def currency(x):
    return "${:.2f}".format(x)


# YES=NO FUNCTION


def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this field cannot be blank. Please try again")
        else:
            return response


def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# STRING CHECKER FUNCTION


def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# DICTIONARIES TO HOLD SUSHI PROGRAM DETAILS
# square brackets [] are used to define various data structures in my main program functions
# which I can customise different variables, such as lists, indexing, slicing, and more

all_sushi = []
all_sides = []
SUSHI_SOLD_LIST = []
PRICES_LIST = []
SIDE_PICKED = []

mini_movie_dict = {
    "Sushi": all_sushi,
    "Sides Price": all_sides
}

# MAIN ROUTINE FOR FUNCTIONS LATER ON


yes_no_list = ["yes", "no"]
sushi_list = ["salmon", "teriyaki", "california", "vegan"]
all_sushi_costs = [10, 12, 12, 8]
size_list = ["6pack", "8pack"]
side_list = ["miso", "tempura", "soy", "wasabi", "xxx"]
all_sides_costs = [5, 2, 0.5, 0.5]
size_costs = [0, 3, 5]
collection_list = ["pickup", "delivery"]
payment_list = ["cash", "credit"]


# INSTRUCTION FOR SUSHI PROGRAM

def show_instructions(): print('''\n

----- Brian's Sushi Shop -----

----- MENU -----

MAINS

Salmon Sushi (salmon) $10.00
Teriyaki Sushi (teriyaki) $12.00
California Sushi (california) $12.00
Vegan Sushi (vegan) $8.00

SIDES

Miso Soup (miso) $5.00
Shrimp Tempura (tempura) $2.00
Soy Sauce (soy) $0.50
Wasabi (wasabi) $0.50

----- Instructions -----

For each item of your choice type the corresponding word in the brackets on the right into the input box
eg: if you want Salmon sushi type "salmon"
Choose what size from 6-8 pack you want ($2 surcharge for 8pack)
Choose if you want sides as-well as your main order 
When you have entered all the items you want, please press 'xxx' to finalise your order
You will get an option to either choose pick up or delivery 
If you choose delivery, please supply your address
Once you are done, select a payment method (cash / credit) to confirm your final order total


----------------------------------------------------------------------------------''')


# START OF PROGRAM FUNCTION

print("Welcome to Brian's Sushi Shop!")

# using a strip and title tag I can to change the initial character in each word to uppercase and the
# subsequent characters to lowercase returning new string while the strip() code
# removes any leading, and trailing whitespaces.
want_instructions = string_checker("Do you want to read the "
                                   "instructions and menu) (y/n): ",
                                   1, yes_no_list)
if want_instructions == "yes":
    show_instructions()

# MAIN MENU SUSHI PRICES


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


# SUSHI OPTION FUNCTION

print("Please type the the corresponding titles in the brackets next to the options to choose your desired item, "
      "e.g. \"(Salmon)\" ")
sushi_type = string_checker("Which sushi do you want: ", 1, sushi_list)

if sushi_type == "salmon":
    print("You selected the $10 Salmon Sushi")
    pass

elif sushi_type == "teriyaki":
    print("You selected the $12 Teriyaki Sushi")
    pass

elif sushi_type == "california":
    print("You selected the $10 California Sushi")
    pass

elif sushi_type == "vegan":
    print("You selected the $8 Vegan Sushi")
    pass

sushi_cost = calc_sushi_price(sushi_type)

# SIZE OPTION FUNCTION

size_choice = string_checker("Please choose from 6 Pack (6pack) or 8 pack (8pack) ($2 surcharge): ", 1, size_list)

if size_choice == "6pack":
    print("You have selected 6 pack sushi rolls (no additional cost)".format(sushi_type))
    size = 0
    pass

elif size_choice == "8pack":
    print("You have selected 8 pack sushi rolls ($2 dollar surcharge)".format(sushi_type))
    size = 2
    pass

else:
    size = 0

sushi_cost = sushi_cost + size

# The temp sides function allows the variable to be stored later on
# to assign and swap the other variable to the main function.
which_sides = 'none'
temp_sides = []

# SIDES FUNCTION

want_sides = string_checker("Would you like sides with your order? (y/n): ", 1, yes_no_list)


def sides(): print('''\n

----- SIDES -----

Please select which sides you want by typing in the name from the list below:
Miso Soup (miso) $5.00
Shrimp Tempura (tempura) $2.00
Soy Sauce (soy) $0.50
Wasabi (wasabi) $0.50

-----------------------------------------------------------------------------''')

# The temp_sides list is  used to keep track of the side dishes that the user has selected for their sushi side order.
# The append() method is a built-in method for listing as it adds the specified element to the end of the list,
# keeping track of the users side dishes.


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

temp_list = []

# LIST OF DETAILS FOR CUSTOMER

PRICES_LIST.append(sushi_cost)
SIDE_PICKED.append(temp_sides)
SUSHI_SOLD_LIST.append(temp_list)


# ORDER SUMMARY FUNCTION

print("----- ORDER SUMMARY -----")

# The curly braces {} inside the string serve as placeholders for values where
# the f" " method is called on the string to replace these placeholders with the provided values that are put in the {}
print("Your Order: ")
print(f"A {size_choice} {sushi_type} sushi with the Sides of {temp_sides} for a total cost of ${sushi_cost:.2f}")

# PAYMENT FUNCTION

print("-----PAYMENT CHOICE-----")

pay_method = string_checker("Would you like to pay in cash or credit (%1.5 fee): ", 1, payment_list)

# using the ${:.2f} currency function I can easily manipulate it by getting the total sushi_cost
# and * multiplying however many percent I need to deduct based on their options

if pay_method == "cash":
    final_cost = sushi_cost * 1
    print(f"Paying with cash. Your final cost remains at ${final_cost:.2f} ")


elif pay_method == "credit":
    final_cost = sushi_cost * 1.015
    print(f"Paying with credit. Your final cost is ${final_cost:.2f} ")

print("---------------------------------------------------------------------------")
print("Thank you for eating at Brian's Sushi Shop, Please come again")
print("---------------------------------------------------------------------------")
