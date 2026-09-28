import timeit

# Wrap the code snippet in a string. Use "setup" to handle imports or variables.
execution_time = timeit.timeit(
    stmt="[i**2 for i in range(10)]",
    number=10000  # Number of times to run the code
)

print(f"Total time for 10,000 runs: {execution_time} seconds")
