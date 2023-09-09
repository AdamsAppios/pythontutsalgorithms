import matplotlib.pyplot as plt
import numpy as np

# Create a range of values for n (e.g., from 1 to 10)
n_values = np.arange(1, 11)

# Define functions for different bounds
upper_bound = 2 * n_values  # Upper bound
lower_bound = 0.5 * n_values  # Lower bound
tight_bound = n_values  # Tight bound

# Create the plot
plt.figure(figsize=(8, 6))

# Plot upper bound
plt.plot(n_values, upper_bound, label='Upper Bound', color='red', linestyle='--')

# Plot lower bound
plt.plot(n_values, lower_bound, label='Lower Bound', color='blue', linestyle='--')

# Plot tight bound
plt.plot(n_values, tight_bound, label='Tight Bound', color='green')

# Label axes
plt.xlabel('n')
plt.ylabel('Function Value')

# Add legend
plt.legend()

# Title and labels
plt.title('Upper Bound vs. Lower Bound vs. Tight Bound')
plt.grid(True)

# Show the plot
plt.show()