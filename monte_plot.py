import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def monte_plotter(points_num, points_array, cir_rad):
    """
    Creates a visualization of the Monte Carlo simulation for estimating π.

    Args:
        points_array (numpy.ndarray): Array of [x, y] coordinates of randomly generated points
        cir_rad (float): Radius of the circle, typically 0.5

    Returns:
        bool: True if plot was successfully displayed or saved, False otherwise
    """
    try:
        # Create a new figure and axes for plotting
        fig = plt.figure()
        ax = plt.axes()

        # Draw the enclosing square with dimensions 1x1
        # The square's bottom-left corner is at (0, 0)
        square_boundary = patches.Rectangle(
            xy=(0, 0), width=1, height=1, ec="b", fc="b"
        )

        # Draw the circle with center at (0.5, 0.5) and specified radius
        # ec = edge color, fill=False means the circle is not filled
        circle_boundary = patches.Circle(xy=(0.5, 0.5), radius=cir_rad, ec="g", fc="c")

        # Add both shapes to the plot
        ax.add_patch(square_boundary)
        ax.add_patch(circle_boundary)

        # Extract x and y coordinates from points array for scatter plot
        x_coords = points_array[:, 0]
        y_coords = points_array[:, 1]

        # Plot all randomly generated points as small red dots
        # s=0.5 controls the size, alpha=0.75 controls transparency
        if points_num < 1024:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=1)
        elif 1024 <= points_num < 65536:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=0.75)
        elif 65536 <= points_num < 262144:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=0.625)
        elif 262144 <= points_num < 1048576:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=0.5)
        elif 1048576 <= points_num < 4194304:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=0.25)
        else:
            plt.scatter(x_coords, y_coords, s=0.5, c="r", marker=".", alpha=0.125)

        # Ensure proper scaling of the plot with equal aspect ratio
        plt.axis("scaled")
        ax.set_aspect("equal")

        try:
            # First try to show the plot interactively
            plt.show()
            return True
        except Exception as e:
            print(f"Warning: Interactive display not available ({str(e)})")
            print("Saving plot as 'monte_carlo_plot.png' instead.")

            # If showing fails, try to save as an image file
            try:
                plt.savefig("monte_carlo_plot.png")
                print(
                    "Plot saved successfully. You can view it in the file 'monte_carlo_plot.png'"
                )
                plt.close(fig)  # Clean up the figure
                return True
            except Exception as e2:
                print(f"Error: Could not save plot: {str(e2)}")
                plt.close(fig)  # Clean up the figure even if saving fails
                return False

    except Exception as e:
        print(f"Error creating plot: {str(e)}")
        return False


# Allow the script to be run standalone for testing
if __name__ == "__main__":
    # Generate some test points (1000 random points)
    test_points = np.array(
        [[np.random.random(), np.random.random()] for _ in range(1000)]
    )
    monte_plotter(test_points, 0.5)
