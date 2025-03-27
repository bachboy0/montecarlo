import numpy as np
from input_validation import asking_plot
from monte_plot import monte_plotter  # Import specific function instead of *


# Display initial welcome message and instructions to the user
def display_welcome_message():
    print(f"Welcome to Monte Carlo")
    print(f"This is a simulation to find Pi using the Monte Carlo Method.")
    print(f"Please enter any natural number to see how the Monte Carlo Method works!")
    print(f"If you would like to quit, enter number 0 anytime.\n")


# Check if a point falls inside or outside the circle and update counters
def point_checker(point, count, rad):
    """
    Determines if a point is inside the circle and updates the counter.

    Args:
        point (array): [x, y] coordinates of the point
        count (array): Counter for points inside [0] and outside [1] the circle
        rad (float): Radius of the circle

    Returns:
        array: Updated counter
    """
    # Calculate the formula for the circle
    # The circle is centered at (rad, rad) with radius rad
    # The formula is (x - center_x)^2 + (y - center_y)^2 - radius^2 <= 0
    # This checks if the point is inside or on the circle
    # The center of the circle is at (rad, rad)
    circle_formula = (point[0] - rad) ** 2 + (point[1] - rad) ** 2 - rad**2
    # Update counter based on whether point is inside or outside the circle
    if circle_formula <= 0:  # Inside circle
        count[0] += 1
    else:  # Outside circle
        count[1] += 1
    return count


# Main simulation function that coordinates the Monte Carlo process
def simulate_monte_carlo(input_number, frequency, radius):
    """
    Runs the Monte Carlo simulation to estimate π.

    Args:
        input_number (int): Number of random points to generate
        frequency (int): Number of simulations to run
        radius (float): Radius of the circle
    """
    # Ask if user wants to plot the points if frequency is 1
    if frequency == 1:
        # Counter for points inside [0] and outside [1] the circle
        counter = np.zeros(2, dtype="int")
        plotting_flag = asking_plot()
        if plotting_flag:
            # When visualization is requested, store all points in memory
            # Preallocate array with correct dimensions for efficiency
            point_list = np.zeros((input_number, 2))
            for i in range(input_number):
                # Generate a single random point in the [0,2*rad) x [0,2*rad) square
                point = np.random.rand(2) * 2 * radius
                # Store the point in the array for later visualization
                point_list[i] = point
                # Update the counter based on point position
                counter = point_checker(point, counter, radius)

            # Calculate and display the final results
            monte_evaluator_once(input_number, counter, radius)

            # Visualize the simulation results
            try_plotting = monte_plotter(input_number, point_list, radius)

            if try_plotting:
                print("Figure generated successfully!")
            else:
                print("Sorry, we could not generate the figure.")
        else:
            # When no visualization is needed, use memory-efficient approach
            # Points are processed one at a time without storing them
            for i in range(input_number):
                point = np.random.rand(2) * 2 * radius  # Generate a random point
                counter = point_checker(point, counter, radius)  # Update counter
            # Calculate and display the final results
            monte_evaluator_once(input_number, counter, radius)
    else:
        counter_multiple = np.zeros((frequency, 2), dtype="int")
        for i in range(frequency):
            for j in range(input_number):
                point = np.random.rand(2) * 2 * radius  # Generate a random point
                counter_multiple[i] = point_checker(point, counter_multiple[i], radius)
        # Calculate and display the final results
        monte_evaluator_multiple(input_number, frequency, counter_multiple, radius)


# Calculate and display the results of the Monte Carlo simulation
def monte_evaluator_once(input_number, count, rad):
    """
    Processes simulation results and calculates π approximation.

    Args:
        input_number (int): Total number of points generated
        count (array): Counter for points inside [0] and outside [1] the circle
        rad (float): Radius of the circle
    """
    # Calculate probability: ratio of points inside circle to total points
    probability_inside_circle = count[0] / input_number

    # Calculate area of circle using actual π value (for comparison)
    area_circle = np.pi * (rad**2)

    # Calculate Pi using the Monte Carlo method:
    # π = 4 * (points inside circle / total points) for unit circle
    monte_pi = 4 * probability_inside_circle

    # Print detailed results to the user
    monte_evaluator_print_once(
        input_number, count, probability_inside_circle, area_circle, monte_pi
    )


def monte_evaluator_multiple(input_number, frequency, count, rad):
    """
    Processes simulation results and calculates π approximation for multiple simulations.

    Args:
        input_number (int): Total number of points generated
        frequency (int): Number of simulations
        count (array): Counter for points inside [0], outside [1] the circle, and frequencies [2]
        rad (float): Radius of the circle
    """
    probabilitiy_array = np.zeros(frequency, dtype="float")
    # Calculate probability for each simulation
    for i in range(frequency):
        probabilitiy_array[i] = count[i][0] / input_number
    # Calculate average probability of points inside the circle
    probability_inside_circle = np.mean(probabilitiy_array)
    # Calculate area of circle using actual π value (for comparison)
    area_circle = np.pi * (rad**2)
    # Calculate average Pi using the Monte Carlo method
    # π = 4 * (average points inside circle / total points) for unit circle
    arerage_monte_pi = 4 * probability_inside_circle

    # Find closest attempt and provide index and value to the circle
    closest_attempt = np.argmin(abs(probabilitiy_array - np.pi))
    # Calculate the closest attempt value
    closest_monte = 4 * probabilitiy_array[closest_attempt]
    # Calculate the error between the closest attempt and actual π
    # Print detailed results to the user
    monte_evaluator_print_multiple(
        frequency,
        input_number,
        probability_inside_circle,
        area_circle,
        arerage_monte_pi,
        closest_attempt,
        closest_monte,
    )


def monte_evaluator_print_once(input_number, count, probability, area_c, monte_pi):
    """
    Processes simulation results and calculates π approximation.

    Args:
        input_number (int): Total number of points generated
        count (array): Counter for points inside [0] and outside [1] the circle
        probability (float): Probability of points inside the circle
        area_c (float): Area of the circle
        monte_pi (float): Approximate value of Pi derived from the Monte Carlo Method
    """
    # Print detailed results to the user
    print(f"Total points: {input_number}")
    print(f"points inside the circle: {count[0]}")
    print(f"points outside the circle: {count[1]}")
    print(f"probability of points inside the circle: {round(probability, 4)}")
    print(f"Area of the circle: {round(area_c, 4)}")
    print(
        f"Approximate value of Pi derived from the Monte Carlo Method: \n{round(monte_pi, 8)}"
    )
    print(f"Pi from Python numpy: \n{round(np.pi, 8)}")
    print(
        f"Error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
        f"{round(abs(monte_pi-np.pi), 8)}"
    )


def monte_evaluator_print_multiple(
    frequency,
    input_number,
    probability,
    area_c,
    arerage_monte_pi,
    closest_attempt,
    closest_monte,
):
    """ "
    "Processes simulation results and calculates π approximation."
    """
    # Print detailed results to the user
    # Print average results
    print(f"Number of simulations: {frequency}")
    print(f"Points for each semulation: {input_number}")
    print(f"Average probability of points inside the circle: {round(probability, 4)}")
    print(f"Average area of the circle: {round(area_c, 4)}")
    print(
        f"Average error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
        f"{round(abs(arerage_monte_pi-np.pi), 8)}"
    )
    print(
        f"Average value of Pi from the Monte Carlo Method: \n{round(arerage_monte_pi, 8)}"
    )
    print(f"Average value of Pi from Python numpy: \n{round(np.pi, 8)}")
    print(
        f"Average error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
        f"{round(abs(arerage_monte_pi-np.pi), 8)}"
    )
    print(f"Closest attempt to Pi: {round(closest_monte, 4)}")
    print(f"Closest attempt index: {closest_attempt}")
    print(f"Closest attempt error: {round(abs(closest_monte - np.pi), 8)}")


# The code above is a complete implementation of the Monte Carlo simulation to estimate π.
# It includes functions for displaying messages, checking points, running the simulation,
# and calculating results. The code is structured to handle both single and multiple simulations,
# and it provides detailed output to the user. The plotting functionality is also included
# but is not fully implemented in this snippet. The code is modular and can be easily extended
# or modified for additional features or improvements.
# The code is designed to be user-friendly and provides clear instructions and feedback.
