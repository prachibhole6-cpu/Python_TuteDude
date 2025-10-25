import math

# Step 1: Ask the user for a number as input
number = float(input("Enter a number: "))

# Step 2: Calculate the square root, natural logarithm, and sine
square_root = math.sqrt(number)
logarithm = math.log(number)
sine_value = math.sin(number)

# Step 3: Display the results
print(f"The square root of {number} is: {square_root}")
print(f"The natural logarithm (log base e) of {number} is: {logarithm}")
print(f"The sine of {number} (in radians) is: {sine_value}")
