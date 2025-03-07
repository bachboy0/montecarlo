def natural_number():
    """
    Accepts and validates a natural number input from the user.
    
    Returns:
        int: The validated natural number
        None: If user enters 0 (exit condition)
        False: If input is invalid
    """
    input_num = None
    string_input = input("Enter natural number: ")
    # Set a limit for the maximum number of points
    limit = 16777216  # 2^24 - limit set due to memory and computation time constraints
    
    # Check if the input is a valid number
    if string_input.isdecimal():
        input_num = int(string_input)
    
    # Throw message if input is invalid
    if input_num is None:
        print("It is not number. Try again.")
        return False
    # Check if the input number is within the allowed limit
    elif input_num >= limit:
        print(f"Number is too large, 1 to {limit-1} is available. Please Try again.")
        return False
    # Exit condition
    elif input_num == 0:
        print("Thank you! See you another time!")
        return None  # Explicitly return None
    else:
        return input_num


def asking_plot():
    """
    Asks the user if they want to display a plot.
    Only accepts 'y' or 'n' as valid inputs and prompts again for invalid inputs.
    
    Returns:
        bool: True if 'y' is entered, False if 'n' is entered
    """
    while True:
        yes_or_no = input("Would you like to plot this?(y/n)")
        yes = yes_or_no == "y" 
        no = yes_or_no == "n"
        
        # Check if input is not a single character
        if len(yes_or_no) != 1:
            print("Please input \'y\' or \'n\' and press enter.")
        # If 'y' was entered
        elif yes:
            return True
        # If 'n' was entered
        elif no:
            return False
        # If a single character other than 'y' or 'n' was entered
        else:
            print("Please input \'y\' or \'n\' and press enter.")