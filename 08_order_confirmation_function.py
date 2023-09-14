# CURRENCY

def currency(x):
    return "${:.2f}".format(x)


yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# this sushi cost will vary in the base python file as it would be set on the customers order, just for an example
# I have set this value to 10
sushi_cost = 10


# STRING CHECKER FUNCTION


def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

# customer order summary confirmation function


while True:
    order_confirm = string_checker("Do you want to confirm your order?) (y/n): ",
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

        elif pay_method == "credit":
            final_cost = sushi_cost * 1.015
            print(f"Paying with credit. Your final cost is ${final_cost:.2f} ")

        print("---------------------------------------------------------------------------")
        print("Thank you for eating at Brian's Sushi Shop, Please come again")
        print("---------------------------------------------------------------------------")

        break

    if order_confirm == "no":
        print("Your order has been canceled, We are sorry if you experienced any inconveniences")
        print("---------------------------------------------------------------------------")
        print("Thank you for visiting Brian's Sushi Shop, Please come again")
        print("---------------------------------------------------------------------------")

        break
