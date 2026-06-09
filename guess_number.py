import random

print("\nI'm thinking of a number between 1 and 100. Try to guess the number I'm thinking of: ")

def check_number(num, number):
    try:
        num = int(num)
        
        if not num:
            print("\nPlease fill the blank!")
        elif (num>100) or (num<1):
            print("\nPlease just enter number between 0 and 100!")
        elif num < number:
            print("\n⬇️ Too low. Guess agian.")
        elif num > number:
            print("\n⬆️ Too high. Guess agin.")
        else:
            print(f"\nNumber {num}. Yes, that's it.🎉")
            return num
    except ValueError:
        print("\n🔢Please just enter valid number!")


def guess_number():
    number = random.randint(0, 100)
    while True:
        num = input("number: ")
        num = check_number(num, number)

        if not num:
            continue
        else:
            while True:
                answer =input("\nWould you like to play again? (yes/no) ")
                if answer.strip().lower() == 'yes':
                    number  = random.randint(0, 100)
                    break
                elif answer.strip().lower() == 'no':
                    print("\nThanks for playing.")
                    return answer
                else:
                    print("\nPlease enter valid answer.")
                    continue
       

if __name__ == '__main__':
    guess_number()


