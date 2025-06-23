# Word Guessing Game
# Creative Feature: The secret word is randomly chosen from a list of words to enhance replayability.

import random

# List of possible secret words
word_list = ['mosiah', 'temple', 'nephi', 'helman', 'moroni', 'zion', 'latter', 'saints', 'faith']

# Choose a secret word randomly
secret_word = random.choice(word_list).lower()

# Initialize variables
guess_count = 0
word_length = len(secret_word)

print("Welcome to the word guessing game!\n")

# Display initial hint with underscores
print("Your hint is:", "_ " * word_length)

# Main game loop
while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check if the guess length matches
    if len(guess) != word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    # Check for correct guess
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break

    # Generate hint
    hint = []
    # Track which letters are unmatched for secondary hint (lowercase)
    unmatched_secret = list(secret_word)

    # First pass: handle exact matches
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
            unmatched_secret[i] = None  # Remove matched letters
        else:
            hint.append(None)  # Placeholder for second pass

    # Second pass: handle correct letters in wrong positions
    for i in range(word_length):
        if hint[i] is None:
            if guess[i] in unmatched_secret:
                hint[i] = guess[i].lower()
                unmatched_secret[unmatched_secret.index(guess[i])] = None
            else:
                hint[i] = "_"

    # Display hint
    print("Your hint is:", " ".join(hint))

