# currency function
# "{:.2f}".format(x) formats the numerical value with two decimal places while the $ sign at the start of the code
# adds a dollar sign to the formatted value. The entire formatted string is returned as a currency amount for the sushi
# program.

def currency(x):
    return "${:.2f}".format(x)


#  not_blank function
# checks that the response from a given question from the end-user in the program has given an answer and is not blank

def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this field cannot be blank. Please try again")
        else:
            return response


# num_check function
# checks that the inputted value is an integer


def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# string checker function
# Validates and processes end-user input based on valid response options

def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# dictionary to hold sushi program details
# square brackets [] are used to define various data structures in my main program functions
# which I can customise different variables, such as lists, indexing, slicing, etc. used throughout the sushi program

all_sushi = []
all_sides = []
PRICES_LIST = []
SIDE_PICKED = []

sushi_program = {
    "Sushi": all_sushi,
    "Sides Price": all_sides
}

# main routing for different functions

yes_no_list = ["yes", "no"]
sushi_list = ["salmon", "teriyaki", "california", "vegan"]
size_list = ["6pack", "8pack"]
side_list = ["miso", "tempura", "soy", "wasabi", "xxx"]
collection_list = ["pickup", "delivery"]
payment_list = ["cash", "credit"]
# Initialize pay_method and final_cost with default values
pay_method = ""
final_cost = 0.0


# the menu for end-users for the sushi program


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
If you choose a collection method of delivery, please supply your address to get your order delivered to your location 
Once you are done, you will receive your order summary
If you confirm your purchase, please select a payment method (cash / credit) to confirm your final order total


----------------------------------------------------------------------------------''')


# start of program function, introduction to the program to end-user

print("Welcome to Brian's Sushi Shop!")

# using a strip and title tag I can to change the initial character in each word to uppercase and the
# subsequent characters to lowercase returning new string while the strip() code
# removes any leading, and trailing whitespaces.
name = not_blank("Please enter the name for your order:  ").strip().title()
print("Welcome", name)
want_instructions = string_checker("Do you want to read the "
                                   "instructions and menu) (yes/no): ",
                                   1, yes_no_list)
if want_instructions == "yes":
    show_instructions()


# main sushi type price calculation


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


# what sushi type customers want function
# using 1 as the num_letters argument in string_checker allows the function to validate end-user input
# based on the first character of the valid options eg: salmon "s",
# making it more convenient and efficient for users to make their selection.

print("Please type the the corresponding titles in the brackets next to the options to choose your desired item, "
      "e.g. \"(salmon)\" ")
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

# how much packs of selected sushi type they want

quantity = num_check(f"How many {sushi_type} sushi packs do you want: ")
# The sushi_cost *= quantity is a shorthand notation for sushi_cost = sushi_cost * quantity
# It multiplies the current value of the sushi_cost by the quantity and assigns the result back to sushi_cost however
# many times the customer wants
sushi_cost *= quantity
print(f"you have selected {quantity} {sushi_type} sushi packs")

# size option function

size_choice = string_checker("Please choose a size from 6 Pack (6pack) or 8 pack (8pack) ($2 surcharge): ",
                             1, size_list)

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

# sushi cost and which sides hold the prices while the temp sides function allows the variable to be stored later on
# to assign and swap the other variable to the main function.
sushi_cost = sushi_cost + size
which_sides = 'none'
temp_sides = []

# customers side dish function

want_sides = string_checker("Would you like sides with your order? (yes/no): ", 1, yes_no_list)


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

SIDE_PICKED.append(temp_sides)
PRICES_LIST.append(sushi_cost)


# customer receipt to minimize repetition of code


def want_receipt():
    print("----- YOUR RECEIPT -----")

    print(f"You have purchased {quantity} {sushi_type} sushi")
    print(f"With the size of {size_choice}")
    print(f"You have purchased the sides, {temp_sides}")
    print(f"Collected by {collection_choice}")
    print(f"You have payed with {pay_method}")
    print(f"For a final cost of ${final_cost:.2f}")

    print("---------------------------------------------------------------------------")
    print("Thank you for eating at Brian's Sushi Shop, Please come again", name)
    print("---------------------------------------------------------------------------")


# the customers collection method of pickup or delivery

print("-----COLLECTION METHOD-----")

collection_choice = string_checker("Do you want your items by pick up (pickup) or delivery (delivery): ", 1,
                                   collection_list)

if collection_choice == "pickup":
    print("you have selected pick up (no additional cost)")
    pass

if collection_choice == "delivery":
    print("You've selected delivery, the $5 surcharge will be added to the final cost")
    address = not_blank("Since you chose the collection method of delivery, "
                        "please enter the address for your order:  ").strip().title()
    print("It will be delivered to", address)
    sushi_cost = sushi_cost + 5


# customers order summary

print("----- ORDER SUMMARY -----")

# The curly braces {} inside the string serve as placeholders for values where
# the f" " method is called on the string to replace these placeholders with the provided values that are put in the {}

print("Your Order: ")
print(f"{quantity} {size_choice} {sushi_type} sushi with the sides of {temp_sides} collected by {collection_choice} "
      f"for a total cost of ${sushi_cost:.2f}")

# customer order functions, including confirmation, payment function and receipt

while True:
    order_confirm = string_checker("Do you want to confirm your order?) (yes/no): ",
                                   1, yes_no_list)
    if order_confirm == "yes":

        # customers payment option of cash or credit

        print("-----PAYMENT CHOICE-----")

        # instead of assigning 1, using len(min ensures full validation of payment method input through the payment list
        # considering entire words of cash and credit, not just the first letter as both have "c" as there first letter"

        pay_method = string_checker("Would you like to pay in cash or credit (%1.5 fee): ",
                                    len(min(payment_list)), payment_list)

        # using the ${:.2f} currency function I can easily manipulate it by getting the total sushi_cost
        # and * multiplying the value I need to deduct based on their chosen option of cash or credit

        if pay_method == "cash":
            final_cost = sushi_cost * 1
            print(f"Paying with cash. Your final cost remains at ${final_cost:.2f} ")
            want_receipt()

        elif pay_method == "credit":
            final_cost = sushi_cost * 1.015
            print(f"Paying with credit. Your final cost is ${final_cost:.2f} ")
            want_receipt()

        break

    if order_confirm == "no":
        print("Your order has been canceled, We are sorry if you experienced any inconveniences")
        print("---------------------------------------------------------------------------")
        print("Thank you for visiting Brian's Sushi Shop, Please come again", name)
        print("---------------------------------------------------------------------------")

        break
