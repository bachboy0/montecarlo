import numpy as np
from input_validation import asking_plot
from monte_plot import *

# Display initial welcome message and instructions
def display_welcome_message():
    print(f"Welcome to Monte Carlo")
    print(f"This is a simulation to find Pi using the Monte Carlo Method.")
    print(f"Please enter any natural number to see how the Monte Carlo Method works!")
    print(f"If you would like to quit, enter number 0.\n")

# Generate random X-Y coordinates within a unit square (0-1 range)
def create_random_point():
    # np.random.rand() generates random values in [0.0, 1.0)
    x_cor = np.random.rand()
    y_cor = np.random.rand()
    return [x_cor, y_cor]

# Check if a point falls inside or outside the circle and update counters
def point_checker(point, count, rad):
    # Circle formula: (x - center_x)² + (y - center_y)² = r²
    # Circle center is (0.5, 0.5) with radius "rad"
    # If circle_formula <= 0, the point is inside or on the circle
    circle_formula = (point[0] - 0.5) ** 2 + (point[1] - 0.5) ** 2 - rad**2
    # inside circle
    if circle_formula <= 0:
        count[0] += 1
    # outside circle
    else:
        count[1] += 1
    return count

# Main simulation function that coordinates the Monte Carlo process
def simulate_monte_carlo(input_number):
    # Counter for points inside [0] and outside [1] the circle
    counter = [0, 0]
    # Set radius to 0.5 (quarter of the unit square)
    circle_radius = 0.5
    # Ask if user wants to plot the points (visual representation)
    plotting_flag = asking_plot()
    
    # Generate coordinates and check position relative to circle
    if plotting_flag:
        # Store points for plotting when visualization is requested
        point_list = []
        for i in range(input_number):
            point_list.append(create_random_point())
            counter = point_checker(point_list[i], counter, circle_radius)
        # Plot the points if plotting_flag is True
        try_plotting = monte_plotter(point_list, circle_radius)
        if try_plotting:
            print("Figure generated successfully!")
        else:
            print("Sorry, we could not generate the figure.")
    else:
        # More efficient version when no visualization is needed
        # Doesn't store points in memory, just counts them
        for i in range(input_number):
            counter = point_checker(create_random_point(), counter, circle_radius)
            
    # Calculate and display the results
    monte_evaluator(input_number, counter, circle_radius)

# Calculate and display the results of the Monte Carlo simulation
def monte_evaluator(input_number, count, rad):
    # Calculate Probability: ratio of points inside circle to total points
    probability_inside_circle = count[0]/input_number
    
    # Calculate area of circle using actual π value (for comparison)
    area_circle = np.pi*(rad**2)
    
    # Calculate Pi using the Monte Carlo method:
    # For our case with circle radius rad and square size 1x1:
    # π = probability_inside_circle / rad²
    monte_pi = probability_inside_circle/(rad**2)
    
    # Print results
    print(f"\nAttempts: {input_number}")
    print(f"Points inside the circle: {count[0]}")
    print(f"Points outside the circle: {count[1]}")
    print(f"Probability of points inside the circle: {round(probability_inside_circle, 4)}")
    print(f"Area of the circle: {round(area_circle, 4)}")
    print(f"Approximate value of Pi derived from the Monte Carlo Method: \n{round(monte_pi, 8)}")
    print(f"Pi from Python numpy: \n{round(np.pi, 8)}")
    print(f"Error between Pi from Python numpy and Pi from the Monte Carlo Method: \n"
          f"{round(abs(monte_pi-np.pi), 8)}")