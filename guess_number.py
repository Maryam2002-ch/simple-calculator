import random

def check_number(user_input, target):
    """Check if user's guess is correct, too low, or too high."""
    try:
        num = int(user_input)
        
        if (num>100) or (num<1):
            print("\nPlease just enter number between 0 and 100!")
            return None

        elif num < target:
            print("\n⬇️ Too low. Guess again.")
            return None

        elif num > target:
            print("\n⬆️ Too high. Guess again.")
            return None
        else:
            print(f"\n🎉 {num} is correct! You got it!")
            return num
    except ValueError:
        print("\n🔢Please just enter valid number!")
        return None

def guess_number():
    """Main game loop"""
    print("\n🤔 I'm thinking of a number between 1 and 100. Try to guess the number I'm thinking of: ")
    
    while True:
        target = random.randint(1, 100)

        while True:
            user_input = input("\nYour guess: ")
            result = check_number(user_input, target)
            
            if result is None:
                continue  # Wrong guess, ask again
            else:
                # Correct guess, ask for replay
                while True:
                    replay = input("\n🔄 Would you like to play again? (yes/no) ").strip().lower()
                    if replay == 'yes':
                        break  # Start new game
                    elif replay == 'no':
                        print("\n👋 Thanks for playing! Have a great day ☺️")
                        return
                    else:
                        print("\n❓ Please enter 'yes' or 'no'!")
                break  # Exit inner loop to start new game

if __name__ == '__main__':
    guess_number()


