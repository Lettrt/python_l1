#task1
num = int(input('Enter your number: '))

if num > 0:
    print(f'{num} is positive.')
elif num < 0:
    print(f'{num} is negative.')
else:
    print(f'{num} is zero.')

if num % 2 == 0:
    print(f'{num} is even.')
elif num == 0:
    print(f'{num} is still zero.')
else:
    print(f'{num} is odd.')


#task2
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

if num_2 == 0:
    print('Some troubles.')
elif num_1 % num_2 == 0:
    print('Divided without.')
else:
    print('Divided with.')

