#importing operators to caculating
from operators import plus_operator, minus_operator, time_operator, divided_operator

print("This is a simple calculator. If you want to quit, enter 'q'.")

operators = ['+', '-', '*', '/']    #define list of operators for checking entry operator

while True:
    number1 = input('\nEnter first number: ')   #getting first number
       
    #checking if user wants to quit
    if number1.strip().lower() == 'q':      
        print("\nHave a good day!")
        break

    operator = input('Enter operator(+, -, *, /): ')    #getting operator
    
    #check if user wants to quit
    if operator.strip().lower() == 'q':
        print("\nHave a good day!")
        break

    number2 = input('Enter second number: ')    #gettin second number
    
    #check if user wants to quit
    if number2.strip().lower() == 'q':
        print("\nHave a good day!")
        break
    
    #check operator to calculating
    if operator.strip() in operators:
        if operator.strip() == '+':
            answer = plus_operator(number1, number2)
        elif operator.strip() == '-':
            answer = minus_operator(number1, number2)
        elif operator.strip() == '*':
            answer = time_operator(number1, number2)
        elif operator.strip() == '/':
            answer = divided_operator(number1, number2)
    
    #check if user doesn't enter any operator
    elif operator.strip() not in operators:
        print("\nPlease enter valid operator!")
    else:
        print("\nPlease enter valid operator!")

        
    
