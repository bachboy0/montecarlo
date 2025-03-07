import numpy as np
from input_validation import asking_plot
from monte_plot import monte_plotter  # Import specific function instead of *


# Display initial welcome message and instructions to the user
def display_welcome_message():
    print(f"Welcome to Monte Carlo")
    print(f"This is a simulation to find Pi using the Monte Carlo Method.")
    print(f"Please enter any natural number to see how the Monte Carlo Method works!")
    print(f"If you would like to quit, enter number 0.\n")


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
    # Circle formula: (x - center_x)² + (y - center_y)² = r²
    # Circle center is (0.5, 0.5) with radius "rad"
    # If circle_formula <= 0, the point is inside or on the circle
    circle_formula = (point[0] - 0.5) ** 2 + (point[1] - 0.5) ** 2 - rad**2
    # Update counter based on whether point is inside or outside the circle
    if circle_formula <= 0:  # Inside circle
        count[0] += 1
    else:  # Outside circle
        count[1] += 1
    return count


# Main simulation function that coordinates the Monte Carlo process
def simulate_monte_carlo(input_number):
    """
    Runs the Monte Carlo simulation to estimate π.
    
    Args:
        input_number (int): Number of random points to generate
    """
    # Counter for points inside [0] and outside [1] the circle
    counter = np.zeros(2, dtype="int")
    # Set radius to 0.5 (half of the unit square side length)
    circle_radius = 0.5
    # Ask if user wants to plot the points (visual representation)
    plotting_flag = asking_plot()

    # Generate coordinates and check position relative to circle
    if plotting_flag:
        # When visualization is requested, store all points in memory
        # Preallocate array with correct dimensions for efficiency
        point_list = np.zeros((input_number, 2))
        for i in range(input_number):
            # Generate a single random point in the [0,1) x [0,1) square
            point = np.random.rand(2)
            # Store the point in the array for later visualization
            point_list[i] = point
            # Update the counter based on point position
            counter = point_checker(point, counter, circle_radius)
        
        # Visualize the simulation results
        try_plotting = monte_plotter(point_list, circle_radius)
        if try_plotting:
            print("Figure generated successfully!")
        else:
            print("Sorry, we could not generate the figure.")
    else:
        # When no visualization is needed, use memory-efficient approach
        # Points are processed one at a time without storing them
        for i in range(input_number):
            point = np.random.rand(2)  # Generate a random point
            counter = point_checker(point, counter, circle_radius)  # Update counter

    # Calculate and display the final results
    monte_evaluator(input_number, counter, circle_radius)


# Calculate and display the results of the Monte Carlo simulation
def monte_evaluator(input_number, count, rad):
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
    # For circle with radius rad in unit square: π = probability_inside_circle / rad²
    monte_pi = probability_inside_circle / (rad**2)

    # Print detailed results to the user
    print(f"\nAttempts: {input_number}")
    print(f"Points inside the circle: {count[0]}")
    print(f"Points outside the circle: {count[1]}")
    print(f"Probability of points inside the circle: {round(probability_inside_circle, 4)}")
    print(f"Area of the circle: {round(area_circle, 4)}")
    print(f"Approximate value of Pi derived from the Monte Carlo Method: \n{round(monte_pi, 8)}")
    print(f"Pi from Python numpy: \n{round(np.pi, 8)}")
    print(f"Error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
          f"{round(abs(monte_pi-np.pi), 8)}")