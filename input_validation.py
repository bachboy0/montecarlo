def get_natural_number_input(limit):
    """
    Accepts and validates a natural number input from the user.

    Returns:
        int: The validated natural number
        None: If user enters 0 (exit condition)
        False: If input is invalid
    """
    print(f"You can enter natural number 1 to {limit-1}")
    string_input = input("Enter natural number: ")
    if string_input == "0":
        print("Thank you! See you another time!")
        return None
    # Check if the input string contains only digits (is a valid number)
    elif string_input.isdecimal():
        input_num = int(string_input)
        return limit_check(input_num, limit)
    else:
        print("Unknown error occurred.")


def set_radius(limit):
    """
    Accepts and validates radius input from the user.

    Returns:
        float: The validated natural number
        None: If input is invalid
    """
    print("You can enter radius over 0 to 64")
    radius_input = input("Enter number: ")
    # Check if the input string is number
    if isfloat(radius_input):
        input_num = float(radius_input)
        return limit_check(input_num, limit)
    elif radius_input == "0":
        print("Thank you! See you another time!")
        return None
    else:
        print("Invalid input. Please enter a valid number.")
        print("Going back to the beginning of the program.\n")
        return None


def limit_check(input_num, limit):
    # Check if the input number is within the allowed limit
    if input_num >= limit:
        print(f"Number is too large, 1 to {limit-1} is available.")
        print("Going back to the beginning of the program.\n")
        return False
    # Valid natural number input
    else:
        print(f"{input_num} is entered.\n")
        return input_num


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return None
    else:
        return True


def asking_plot():
    """
    Asks the user if they want to display a plot.
    Only accepts 'y' or 'n' as valid inputs and prompts again for invalid inputs.

    Returns:
        bool: True if 'y' is entered, False if 'n' is entered
    """
    print(
        "\nCAUTION: Plotting may take a long time if you input over a million points."
    )
    print("Ensure your computer has sufficient performance before proceeding.")

    while True:
        yes_or_no = input("\nWould you like to plot this? (y/n): ")
        yes = yes_or_no == "y"
        no = yes_or_no == "n"

        # Validate user input and handle different cases
        if len(yes_or_no) != 1:
            # Input is not a single character
            print("Please input 'y' or 'n' and press enter.")
        elif yes:
            # User wants to plot the simulation
            return True
        elif no:
            # User does not want to plot the simulation
            return False
        else:
            # Input is a single character but not 'y' or 'n'
            print("Please input 'y' or 'n' and press enter.")
