import numpy as np

marks = np.array([
    [65, 70, 75],
    [80, 85, 90],
    [55, 60, 65]
])

# Add 5 grace marks to Subject 1 (column index 0)
marks[:, 0] += 5

# Transpose matrix
transposed = marks.T

# Convert to single row
report = transposed.flatten()

print("Updated Marks:\n", marks)
print("\nTransposed Matrix:\n", transposed)
print("\nSingle Row Format:\n", report)