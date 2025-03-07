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
    # Set a limit for the maximum number of points to prevent memory issues
    limit = 16777216  # 2^24 - limit set due to memory and computation time constraints
    
    # Check if the input string contains only digits (is a valid number)
    if string_input.isdecimal():
        input_num = int(string_input)
    
    # Process the input value and determine what to return
    if input_num is None:
        # Input couldn't be converted to an integer
        print("It is not a number. Try again.")
        return False
    # Check if the input number is within the allowed limit
    elif input_num >= limit:
        print(f"Number is too large, 1 to {limit-1} is available. Please try again.")
        return False
    # Exit condition - user chose to quit
    elif input_num == 0:
        print("Thank you! See you another time!")
        return None  # Explicitly return None to signal program exit
    # Valid natural number input
    else:
        return input_num


def asking_plot():
    """
    Asks the user if they want to display a plot.
    Only accepts 'y' or 'n' as valid inputs and prompts again for invalid inputs.
    
    Returns:
        bool: True if 'y' is entered, False if 'n' is entered
    """
    print("\nCAUTION: Plotting may take a long time if you input over a million points.")
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