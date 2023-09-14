# STRING CHECKER FUNCTION

def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

# MAIN ROUTINE FOR FUNCTIONS


which_sides = 'none'
temp_sides = []
yes_no_list = ["yes", "no"]
size_list = ["6pack", "8pack"]
side_list = ["miso", "tempura", "soy", "wasabi", "xxx"]


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


# SIZE OPTION FUNCTION

size_choice = string_checker("Please choose from 6 Pack (6pack) or 8 pack (8pack) (+$2): ", 1, size_list)

if size_choice == "6pack":
    print("You have selected 6 pack sushi rolls (no additional cost)")
    size = 0

elif size_choice == "8pack":
    print("You have selected 8 pack sushi rolls ($2 dollar surcharge)")
    size = 2

else:
    size = 0
