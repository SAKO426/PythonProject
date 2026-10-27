# Calculator Bug
# Task: Use the debugger to find the logic error in this calculator
# The program should add two numbers, but it's giving wrong results

def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

# Main program
print("=== Simple Calculator ===")
num1 = 5
num2 = 3

# Calculate addition
sum_result = add_numbers(num1, num2)
print(f"{num1} + {num2} = {sum_result}")

# Calculate multiplication
multiply_result = multiply_numbers(num1, num2)
print(f"{num1} * {num2} = {multiply_result}")

# Expected output:
# 5 + 3 = 8
# 5 * 3 = 15
#
# But you're getting wrong results! Use the debugger to find why.