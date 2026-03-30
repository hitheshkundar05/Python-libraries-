import numpy as np

# Original Traffic Matrix
T = np.array([
    [100, 50],
    [80, 120]
])

print("Original Traffic Matrix:")
print(T)

# Signal Transformation Matrix
S = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

print("\nSignal Transformation Matrix:")
print(S)

# Optimized Traffic Matrix
T_new = np.dot(S, T)

print("\nOptimized Traffic Matrix:")
print(T_new)

# Total vehicles before and after optimization
print("\nTotal vehicles before optimization:", np.sum(T))
print("Total vehicles after optimization:", np.sum(T_new))