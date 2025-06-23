import random

keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1,100)
    print(f"The random number was: {secret_number}")

    secret_number = 42

    guess_count = 0
    guess = -1




    while guess != secret_number:
        guess = int(input("what is your guess?"))
        guess_count = guess_count + 1
        print(f"Your guess is {guess}, you have made {guess_count} guesses so far.")
        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")    
        else:
            print("You guess it!")
    print(f"It took you {guess_count} guesses")        

    print("Will you ike to play again (yes/no)?")