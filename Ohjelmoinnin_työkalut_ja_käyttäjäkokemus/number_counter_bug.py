# Number Counter Bug
# Task: Use the debugger to find why the counter gives wrong results
# The program should count how many numbers are greater than 10

def count_large_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 10:
            count = count + 1
    return count

# Main program
print("=== Number Counter ===")
test_numbers = [5, 15, 8, 20, 10, 3, 12, 7, 18]

print(f"Numbers: {test_numbers}")
large_count = count_large_numbers(test_numbers)
print(f"Numbers greater than 10: {large_count}")

# Expected output:
# Numbers: [5, 15, 8, 20, 10, 3, 12, 7, 18]
# Numbers greater than 10: 4
#
# But you're getting the wrong count! Use the debugger to find the logic error.