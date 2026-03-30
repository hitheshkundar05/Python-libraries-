import numpy as np

base_sales = np.array([
    [100],
    [150],
    [200]
])

growth_factor = np.array([
    [1.1, 0,   0],
    [0,   1.2, 0],
    [0,   0,   1.3]
])

# Multiply matrices
updated_sales = growth_factor @ base_sales

# Convert to single row
report = updated_sales.flatten()

print("Updated Sales:\n", updated_sales)
print("\nSingle Row Format:\n", report)