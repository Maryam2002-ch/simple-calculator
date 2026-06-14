#importing operators to caculating
from operators import plus_operator, minus_operator, time_operator, divided_operator

def check_quit(user_input):
    """Check if user wants to quit"""
    if user_input.strip().lower() == 'q':
        print("\n👋 Have a good day!")
        return True
    return False

print("This is a simple calculator. If you want to quit, enter 'q'.")

operators = ['+', '-', '*', '/']    #define list of operators for checking entry operator

while True:
    number1 = input('\nEnter first number: ')   #getting first number
       
    #checking if user wants to quit
    if check_quit(number1):
        break

    operator = input('Enter operator(+, -, *, /): ')    #getting operator
    
    #check if user wants to quit
    if check_quit(operator):
        break

    number2 = input('Enter second number: ')    #gettin second number
    
    #check if user wants to quit
    if check_quit(number2):
        break
    
    #check operator to calculating
    if operator.strip() in operators:
        if operator.strip() == '+':
            plus_operator(number1, number2)
        elif operator.strip() == '-':
            minus_operator(number1, number2)
        elif operator.strip() == '*':
            time_operator(number1, number2)
        elif operator.strip() == '/':
            divided_operator(number1, number2)
    
    #check if user doesn't enter any operator
    elif operator.strip() not in operators:
        print("\nPlease enter valid operator!")
    else:
        print("\nPlease enter valid operator!")
