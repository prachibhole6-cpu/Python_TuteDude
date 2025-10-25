# Function to calculate the factorial of a number
def factorial(n):
    # Initialize the result to 1 (as 0! and 1! both are 1)
    result = 1
    # Loop to multiply result by each number from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number to calculate the factorial of
number = 5

# Calling the factorial function and printing the result
print(f"The factorial of {number} is {factorial(number)}")
