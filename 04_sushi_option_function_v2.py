sushi_list = ["salmon", "teriyaki", "california", "vegan"]

# num_check function
# checks that the inputted value is an integer


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

# how much selected sushi type they want

quantity = num_check(f"How many {sushi_type} sushi packs do you want: ")
# The sushi_cost *= quantity is a shorthand notation for sushi_cost = sushi_cost * quantity
# It multiplies the current value of the sushi_cost by the quantity and assigns the result back to sushi_cost however
# many times the customer wants
sushi_cost *= quantity
print(f"you have selected {quantity} {sushi_type} sushi packs")
