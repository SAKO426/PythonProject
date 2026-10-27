# Grade Checker Bug
# Task: Use the debugger to find why the grade checker gives wrong grades
# The program should assign letter grades based on percentage scores

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Main program
print("=== Grade Checker ===")
test_scores = [95, 85, 75, 65, 55]

for score in test_scores:
    grade = get_grade(score)
    print(f"Score: {score}% -> Grade: {grade}")

# Expected output:
# Score: 95% -> Grade: A
# Score: 85% -> Grade: B
# Score: 75% -> Grade: C
# Score: 65% -> Grade: D
# Score: 55% -> Grade: F
#
# But you're getting wrong grades! Use the debugger to find the logic error.