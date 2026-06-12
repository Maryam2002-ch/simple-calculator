from operators import plus_operator, minus_operator, time_operator, divided_operator

print("This is a simple calculator. If you want to quit, enter 'q'.")

operators = ['+', '-', '*', '/']

while True:
    number1 = input('\nEnter number 1: ')
    if number1.strip().lower() == 'q':
        print("\nHave a good day!")
        break

    number2 = input('Enter number 2: ')
    if number2.strip().lower() == 'q':
        print("\nHave a good day!")
        break

    operator = input('Enter operator(+, -, *, /): ')

    if operator.strip() == '+':
        answer = plus_operator(number1, number2)
        print(f"Answer: {answer}")
    
    elif operator.strip() == '-':
        answer = minus_operator(number1, number2)
        print(f"Answer: {answer}")

    elif operator.strip() == '*':
        answer = time_operator(number1, number2)
        print(f"Answer: {answer}")

    elif operator.strip() == '/':
        answer = divided_operator(number1, number2)
        print(f"Answer: {answer}")
    
    elif operator.strip().lower() == 'q':
        print("\nHave a good day!")
        break

    elif operator.strip() not in operators:
        print("\nPlease enter valid operator!")


        
    
