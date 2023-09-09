import matplotlib.pyplot as plt
import numpy as np

# Create a range of values for n (e.g., from 1 to 10)
n_values = np.arange(1, 11)

# Define the functions for 1, n, and n^2
constant_function = np.ones_like(n_values)
linear_function = n_values
quadratic_function = n_values ** 2

# Create a new figure
plt.figure(figsize=(12, 4))

# Plot 1
plt.subplot(131)
plt.plot(n_values, constant_function, label='1')
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Constant Function (Θ(1))')
plt.legend()

# Plot n
plt.subplot(132)
plt.plot(n_values, linear_function, label='n', color='orange')
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Linear Function (Θ(n))')
plt.legend()

# Plot n^2
plt.subplot(133)
plt.plot(n_values, quadratic_function, label='n^2', color='green')
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Quadratic Function (Θ(n^2))')
plt.legend()

# Adjust subplot spacing
plt.tight_layout()

# Show the plots
plt.show()