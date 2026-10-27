# Word Length Bug
# Task: Use the debugger to find why the word length calculation is wrong
# The program should find the longest word in a list

def find_longest_word(words):
    longest_word = ""
    max_length = 0

    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_word = word

    return longest_word, max_length

# Main program
print("=== Longest Word Finder ===")
word_list = ["cat", "hippopotamus", "elephant", "dog", "butterfly", "bird"]

longest, length = find_longest_word(word_list)
print(f"Words: {word_list}")
print(f"Longest word: '{longest}' (length: {length})")

# Expected output:
# Words: ['cat', 'elephant', 'dog', 'butterfly', 'bird']
# Longest word: 'butterfly' (length: 9)
#
# But you're getting the wrong result! Use the debugger to find the logic error.