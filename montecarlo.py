import numpy as np

# Initial message for start
def prologue():
    print(f"Welcome to Monte Carlo")
    print(f"This is a simulation to find Pi using the Monte Carlo Method.")
    print(f"Please enter any natural number to see how the Monte Carlo Method works!")
    print(f"If you would like to quit, enter number 0.\n")

# Generate random X-Y coordinates
def point_coordinate():
    # Generate random X-Y coordinates
    x_cor = np.random.rand()
    y_cor = np.random.rand()
    return [x_cor, y_cor]

# Logic to determine if point is inside the circle
def logics(point, count, rad):
    # Circle general form center is 0.5
    # due to random number range being 0.0 <= random < 1.0
    circle_formula = (point[0] - 0.5) ** 2 + (point[1] - 0.5) ** 2 - rad**2
    # inside circle
    if circle_formula <= 0:
        count[0] += 1
    # outside circle
    else:
        count[1] += 1
    return count

# Monte Carlo Simulator
def monte_carlo(input_number):
    # Counter for points inside and outside the circle
    counter = [0, 0]
    # Set radius
    rad = 0.5

    # Generate coordinates and apply logic
    for i in range(input_number):
        logics(point_coordinate(), counter, rad)
    
    # Call monte_result to calculate and display the results
    monte_result(input_number, counter, rad)

# Calculate and display the results of the Monte Carlo simulation
def monte_result(input_number, count, rad):
    # Calculate Probability
    monte_probability = count[0]/input_number
    # Calculate area of circle
    area_circle = np.pi*(rad**2)
    # Calculate Pi from the Monte Carlo Method
    montepi = monte_probability/(rad**2)
    # Print results
    print(f"\nAttempts: {input_number}")
    print(f"Points inside the circle: {count[0]}")
    print(f"Points outside the circle: {count[1]}")
    print(f"Probability of points inside the circle: {monte_probability:.4f}")
    print(f"Area of the circle: {area_circle:.4f}")
    print(f"Approximate value of Pi derived from the Monte Carlo Method: \n{montepi:.8f}")
    print(f"Pi from Python numpy: \n{np.pi:.8f}")
    print(f"Error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
          f"{abs(montepi-np.pi):.8}")

# Main function to run the Monte Carlo simulation
def main():
    prologue()
    while True:
        string_input = input("Enter natural number: ")

        # Check if the input is a valid number
        if not string_input.isdecimal():
            print("It is not number. Try again.")
        else:
            input_num = int(string_input)

        # Exit condition
        if input_num == 0:
            print("Thank you! See you another time!")
            break

        # Set a limit for the maximum number of points
        limit = 16777216
        # Check if the input number is within the allowed limit
        if input_num >= limit:
            print(f"Number is too large, 1 to {limit-1} is available. Please Try again.")
        else:
            # Run the Monte Carlo simulation
            monte_carlo(input_num)
            print(f"\nIf you would like to quit, enter number 0 and press Enter.\n")

main()