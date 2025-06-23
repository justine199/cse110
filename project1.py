# Creative Addition: Added extra parts to the story including more user inputs, and automatically choosing "a" or "an" before a word based on its first letter.

def get_article(story):
    """Returns 'an' if the story starts with a vowel sound, otherwise 'a'."""
    return "an" if story[0].lower() in 'aeiou' else "a"

print("Please enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")


print("\nYour story is:\n")

print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print(f"right in front of my family.")


