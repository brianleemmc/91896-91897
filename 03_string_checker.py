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

# start of program function, introduction to the program to end-user


print("Welcome to Brian's Sushi Shop!")

# using a strip and title tag I can to change the initial character in each word to uppercase and the
# subsequent characters to lowercase returning new string while the strip() code
# removes any leading, and trailing whitespaces.
want_instructions = string_checker("Do you want to read the "
                                   "instructions and menu) (yes/no): ",
                                   1, yes_no_list)
