import numpy as np

# 1D NumPy Array
x = np.array([1, 2, 3, 4, 5, 6])
print("NumPy 1D:", x)
print("Type:", type(x))

# 3D NumPy Array (Corrected syntax for a collection of 2D matrices)
# If you wanted a single 2D array, it should be: np.array([[1, 2, 3], [4, 5, 6]])
y_np = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[8, 9, 10], [11, 12, 13]]
])
print("\nNumPy 3D Array Shape:", y_np.shape)
print(y_np)

# Python List Example
y_list = [1, 2, 3, 4, 5, 6]
print("\nPython List:", y_list)
print("Type:", type(y_list))
