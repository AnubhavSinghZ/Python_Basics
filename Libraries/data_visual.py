import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs

# Define the x-axis values
x = [1, 2, 3, 4, 5]

# Define the y-axis values
y = [2, 4, 6, 8, 10]

# Plot a line graph using x and y values
# label gives the name of the line
# color sets the line color to blue
plt.plot(x, y, label="Growth", color="blue")

# Set the label for the x-axis
plt.xlabel("Time")

# Set the label for the y-axis
plt.ylabel("Value")

# Set the title of the graph
plt.title("Simple Line Plot")

# Display the legend on the graph
plt.legend()

# Display the graph
plt.show()
