import random

r = lambda: random.randint(15, 20)
d = lambda: random.randint(15, 20)
wins, losses = 0, 0

def play_game():
    hp, dmg = r(), r()
    name = input("\nWhat's your name: ")
    print(f"These are your stats / hp: {hp}, dmg: {dmg}")

    if input("Choose road 1 or road 2: ").strip() == "1":
        ehp, edmg = d(), d()
        print(f"The enemy has appeared / hp: {ehp}, dmg: {edmg}")

        if input("1 = Attack / 2 = Flee : ").strip() == "1":
            hp, ehp = hp - edmg, ehp - dmg
            print(f"You've dealt {dmg}, You've received {edmg}")
            print("You've won!" if hp > ehp else "Game over!")
        else:
            print("You fled successfully!")
    else:
        print("You've stumbled across the safe path.")

    # Call the function again to restart
    again = input("\nWould you like to try again? (yes/no): ").strip().lower()
    if again in ["yes", "y"]:
        play_game()

# Start the game for the first time
play_game()