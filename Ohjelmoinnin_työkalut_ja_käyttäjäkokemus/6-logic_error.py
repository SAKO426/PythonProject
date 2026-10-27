# Exercise 5: Logic Error
# Task: Fix the logic error in this code
# The program should check if a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
         return "odd"

# Main program
test_numbers = [2, 3, 4, 5, 6]

for number in test_numbers:
    result = check_even_odd(number)
# There's a logic error in the print statement
    print(f"{number} is {result}") # This should work correctly

# Expected output:
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
# 6 is even