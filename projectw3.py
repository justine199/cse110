# Text-Based Adventure Game
# Added Creativity: This game features a hidden choice ("DANCE") at one branch that unlocks a secret whimsical path.

def adventure_game():
    print("You wake up in an ancient ruin, surrounded by mossy stone walls. In front of you lie two items: a SWORD and a MAP. Which one do you pick?")
    first_choice = input("Type SWORD or MAP: ").strip().lower()

    if first_choice == "sword":
        print("\nYou pick up the sword. As you swing it to test its weight, a stone door grinds open. A goblin charges at you!")
        print("Do you want to FIGHT the goblin, TALK to it, or RUN away?")
        second_choice = input("Type FIGHT, TALK, or RUN: ").strip().lower()

        if second_choice == "fight":
            print("\nYou engage the goblin in a fierce duel and emerge victorious. Behind him lies a treasure chest.")
            print("Do you want to OPEN the chest or LEAVE it alone?")
            third_choice = input("Type OPEN or LEAVE: ").strip().lower()

            if third_choice == "open":
                print("\nInside the chest, you find ancient armor. You are now the guardian of the ruins. The end.")
            elif third_choice == "leave":
                print("\nYou walk away with honor, deciding not to risk it. The ruins echo behind you. The end.")
            else:
                print("That's not a valid choice. Game over.")

        elif second_choice == "talk":
            print("\nYou try to talk to the goblin. Surprisingly, it's fluent in Common Tongue and gives you a riddle.")
            print("Do you want to ANSWER the riddle, IGNORE it, or DANCE to confuse it?")
            third_choice = input("Type ANSWER, IGNORE, or DANCE: ").strip().lower()

            if third_choice == "answer":
                print("\nYou solve the riddle, impressing the goblin. He shows you a secret exit. You escape safely. The end.")
            elif third_choice == "ignore":
                print("\nThe goblin is insulted and storms off. You're alone in the ruins again. The end.")
            elif third_choice == "dance":
                print("\nYou dance like your life depends on it. The goblin joins you. A disco ball drops from the ceiling. You now rule Goblintown. The end.")
            else:
                print("That's not a valid choice. Game over.")

        elif second_choice == "run":
            print("\nYou sprint away, sword still in hand, and fall into a hidden pit. Game over.")
        else:
            print("That's not a valid choice. Game over.")

    elif first_choice == "map":
        print("\nYou pick up the map. It reveals two routes: one through the SWAMP and one through the MOUNTAIN.")
        second_choice = input("Do you take the SWAMP or the MOUNTAIN route? ").strip().lower()

        if second_choice == "swamp":
            print("\nThe swamp is dark and murky. You see a boat, a raft, and a path on foot.")
            third_choice = input("Do you take the BOAT, the RAFT, or go on FOOT? ").strip().lower()

            if third_choice == "boat":
                print("\nThe boat was cursed! You turn into a frog. Ribbit. The end.")
            elif third_choice == "raft":
                print("\nThe raft safely takes you to the other side. You find an ancient temple. The end.")
            elif third_choice == "foot":
                print("\nYou slog through the swamp and emerge tired but wiser. The end.")
            else:
                print("That's not a valid choice. Game over.")

        elif second_choice == "mountain":
            print("\nThe mountain trail is steep. You find a sleeping dragon.")
            third_choice = input("Do you SNEAK past, WAKE the dragon, or TAKE a picture? ").strip().lower()

            if third_choice == "sneak":
                print("\nYou sneak by safely and discover a hidden monastery. The end.")
            elif third_choice == "wake":
                print("\nThe dragon is cranky and chases you off the mountain. Game over.")
            elif third_choice == "take a picture":
                print("\nThe dragon wakes up, sees the camera, and smiles. You are now a famous wildlife photographer. The end.")
            else:
                print("That's not a valid choice. Game over.")
        else:
            print("That's not a valid choice. Game over.")

    else:
        print("That's not a valid choice. Game over.")

# Run the game
adventure_game()
