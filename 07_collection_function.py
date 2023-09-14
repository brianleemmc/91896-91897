collection_list = ["pickup", "delivery"]
yes_no_list = ["yes", "no"]

# STRING CHECKER FUNCTION


def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# COLLECTION FUNCTION

print("-----COLLECTION METHOD-----")

collection_choice = string_checker("Do you want your items by pick up (pickup) or delivery (delivery): ", 1,
                                   collection_list)

if collection_choice == "pickup":
    print("you have selected pick up (no additional cost)")
    pass

if collection_choice == "delivery":
    print("You've selected delivery, the $5 surcharge will be added to the final cost")
    address = input("Please enter the address for your order:  ").strip().title()
    print("It will be delivered to", address)
