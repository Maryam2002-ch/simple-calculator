import random

print("\nI'm thinking of a number between 0 and 100. Try to guess the number I'm thinking of: ")

def guess_number():
    number = random.randint(0, 100)
    while True:
        try:
            num = input("Number: ")
            if int(num) < number:
                print("\nToo low. Guess again.")
                continue
            elif int(num) > number:
                print("\nToo high. Guess again.")
                continue
            elif int(num) == number:
                while True:
                    answer =input("\nThat's it. would you like to play again? (yes/no) ")
                    if answer.strip().lower() == 'yes':
                        number  = random.randint(0, 100)
                        break
                    elif answer.strip().lower() == 'no':
                        print("\nThanks for playing.")
                        return answer
                    else:
                        print("\nPlease enter valid answer.")
                        continue
        except ValueError:
            print("\nPlease enter valid number.")
            continue

if __name__ == '__main__':
    guess_number()


