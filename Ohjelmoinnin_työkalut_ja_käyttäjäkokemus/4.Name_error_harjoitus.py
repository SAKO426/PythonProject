# Exercise 3: NameError
# Task: Fix the NameError in this code
# The program should greet the user
def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to our program!")
    print(f"Your name has {len(name)} letters.") # There's a typo here!
greet_user()
# Expected output: Should ask for name and greet properly