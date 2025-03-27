from input_validation import get_natural_number_input, set_radius
from monte_carlogic import display_welcome_message, simulate_monte_carlo


# Main function to run the Monte Carlo simulation
def main():
    """
    Main program loop that handles user input and runs the Monte Carlo simulation.
    Continues until the user chooses to exit by entering 0.
    """
    # Display welcome message with instructions for the user
    display_welcome_message()

    # Continue running until the user chooses to exit
    while True:
        # Get validated user input
        input_check_result = get_natural_number_input(limit=32768)
        if input_check_result is None:
            # Exit condition (user entered 0)
            break
        elif input_check_result is False:
            # Invalid input (not a natural number)
            continue

        # Set radius value
        circle_radius = set_radius(limit=64)
        if circle_radius is None:
            # Exit condition (user entered 0)
            break
        elif circle_radius is False:
            # Invalid input (not a valid radius)
            continue

        # Valid radius was entered, proceed with simulation
        print(f"Circle radius is set to {circle_radius}.\n")
        # Display the number of points to be generated
        print(f"Number of points to be generated: {input_check_result}.\n")
        # Set simulate frequency
        print("\nYou can enter natural number 1 to 256")
        print("If you want to plot this, enter 1.")
        print("If you want to simulate only, enter 2 to 256.")
        print("If you want to quit, enter 0.")

        # Get frequency input from the user
        simulate_frequency = get_natural_number_input(limit=256)
        if simulate_frequency is None:
            break
        elif simulate_frequency is False:
            continue

        # Valid natural number was entered, run the simulation
        simulate_monte_carlo(input_check_result, simulate_frequency, circle_radius)
        # Remind user how to exit the program
        print(f"\nIf you would like to quit, enter number 0 and press Enter.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
