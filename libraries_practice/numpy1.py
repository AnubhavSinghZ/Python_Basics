import numpy as np

# 1D NumPy Array
x = np.array([1, 2, 3, 4, 5, 6])
print("NumPy 1D:", x)
print("Type:", type(x))

# 2D NumPy Array (Matrix with 2 rows and 3 columns)
y_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\nNumPy 2D Array Shape:", y_2d.shape)
print(y_2d)

# 3D NumPy Array (Collection of 2D matrices)
y_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[8, 9, 10], [11, 12, 13]]
])
print("\nNumPy 3D Array Shape:", y_3d.shape)
print(y_3d)

# Python List Example
y_list = [1, 2, 3, 4, 5, 6]
print("\nPython List:", y_list)
print("Type:", type(y_list))
