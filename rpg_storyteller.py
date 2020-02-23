import storyteller_dice

dice = input("How many dice(s) should be rolled? ")
difficulty = input("Difficulty check: ")
storyteller_dice.roll_dice(int(dice), int(difficulty))