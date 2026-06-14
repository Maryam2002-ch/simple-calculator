#define operators functions

def plus_operator(number1, number2):
    """plus two numbers"""
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 + number2
        print(f"\nAnswer: {answer}")
        return answer

def minus_operator(number1, number2):
    """minus two numbers"""
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 - number2
        print(f"\nAnswer: {answer}")
        return answer

def time_operator(number1, number2):
    """multiply to numbers"""
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        answer = number1 * number2
        print(f"\nAnswer: {answer}")
        return answer

def divided_operator(number1, number2):
    """divide two numbers"""
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("\nPlease enter valid numbers!")
        return None
    else:
        try:
            answer =  number1/number2
            print(f"\nAnswer: {answer}")
            return answer
        except ZeroDivisionError:
            print("\nCan not division by zero!")
            return None