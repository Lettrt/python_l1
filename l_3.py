num1 = int(input('Enter 1st number: '))
operater = input('Enter + - * /: ')
num2 = int(input('Enter 2nd number: '))

if operater ==  '+':
    print(num1 + num2)
elif operater == '-':
    print(num1 - num2)
elif operater == '*':
    print(num1 * num2)
elif operater == '/':
    print(num1 / num2)
else:
    print('NOOOOOOOOOOOOOO!')