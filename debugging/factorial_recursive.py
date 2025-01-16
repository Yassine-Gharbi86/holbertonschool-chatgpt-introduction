import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Retrieve the input number from command-line arguments,
# calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)