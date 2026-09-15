import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="Growth", color="blue")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Simple Line Plot")
plt.legend()
plt.show()
