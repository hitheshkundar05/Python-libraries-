import numpy as np

prices = np.array([
    [1000, 1200, 1500],
    [800,  900,  1100],
    [950,  1050, 1300]
])

# Apply 10% discount
discounted = prices * 0.9

# Round values
discounted = np.round(discounted)

# Convert to single row
report = discounted.reshape(1, -1)

print("Discounted Prices:\n", discounted)
print("\nSingle Row Format:\n", report)