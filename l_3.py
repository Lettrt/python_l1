num1 = int(input('Enter 1st number: '))
operator = input('Enter + - * /')
num2 = int(input('Enter 2nd number: '))

if operator == '+':
    result = num1 + num2
    print(f'Result is {result}')

elif operator == '-':
    result = num1 - num2
    print(f'Result is {result}')

elif operator == '*':
    result = num1 * num2
    print(f'Result is {result}')

elif operator == '/':
    result = num1 / num2
    print(f'Result is {result}')

else:
    print('Неправильный оператор!!!')