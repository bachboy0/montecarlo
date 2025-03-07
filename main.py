from input_validation import natural_number
from monte_carlogic import display_welcome_message, simulate_monte_carlo

# Main function to run the Monte Carlo simulation
def main():
    # Display welcome message with instructions for the user
    display_welcome_message()
    
    # Continue running until the user chooses to exit
    while True:
        # Get validated user input
        valid_check = natural_number()
        
        # Check return value from natural_number() function
        if valid_check is None:
            # Exit condition (user entered 0)
            break
        elif isinstance(valid_check, int):
            # Valid natural number was entered, run the simulation
            simulate_monte_carlo(valid_check)
            # Remind user how to exit the program
            print(f"\nIf you would like to quit, enter number 0 and press Enter.\n")
        elif not valid_check:
            # Invalid input case - natural_number() already displayed error message
            # Just continue the loop to get new input
            pass
        else:
            # Unexpected return value (defensive programming)
            print("An unexpected error occurred. Exiting the program.")
            break

# Entry point of the program
if __name__ == "__main__":
    main()