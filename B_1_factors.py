# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("THE ULTIMATE FACTOR FINDER", "-")

    print('''
Please enter an Integer between 1 and 200, and I 
will tell you if it is unity, if it is a prime 
number and its factors
    ''')

# Ask the user for an integer between 1 and 200
def num_check(question):

    error = "Please enter a whole number between 1 and 200\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



def factor(var_to_factor):
    """Generates a list of factors for a given integer"""
    factors_list = []

    # square root the number to work out when to stop looping
    stop = var_to_factor ** 0.5
    stop = int(stop)

    for item in range(0, stop + 1):

        # check to see if the item is a factor
        if to_factor % item == 0:
            factors_list.append(item)

            # calculate partner
            partner = var_to_factor // item

            # add partner to the list (but prevent duplicate entries)
            if partner not in factors_list:
                factors_list.append(partner)


    # return the sorted list
    factors_list.sort()
    return factors_list

# Main routine goes here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <Enter> ot read the instructions"
                          "or press any key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask the user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == 'xxx':
        break

    # get factors for integer that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only"

    # comments for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"
    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    #output
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the Ultimate Factor Finder.")


