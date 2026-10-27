# Exercise 4: TypeError
# Task: Fix the TypeError in this code
# The program should calculate the average of three numbers

def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

# Main program
numbers = [10, 20, 30]
# There's a TypeError here - we're passing a list instead of individual numbers
result = calculate_average(numbers[0], numbers[1], numbers[2])
print(f"The average is: {result}")

# Expected output: The average is: 20.0