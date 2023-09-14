yes_no_list = ["yes", "no"]

# functions


def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this field cannot be blank. Please try again")
        else:
            return response

# start of program function, introduction to the program to end-user


print("Welcome to Brian's Sushi Shop!")

# using a strip and title tag I can to change the initial character in each word to uppercase and the
# subsequent characters to lowercase returning new string while the strip() code
# removes any leading, and trailing whitespaces.
name = not_blank("Please enter the name for your order:  ").strip().title()
print("Welcome", name)
print("Do you want to read the instructions and menu) (y/n): ")
