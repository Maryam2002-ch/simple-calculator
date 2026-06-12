def plus_operator(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 + number2
        return answer

def minus_operator(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 - number2
        return answer

def time_operator(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 * number2
        return answer

def divided_operator(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer =  number1/number2
        return answer