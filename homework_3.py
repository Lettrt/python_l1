    #Задача 1

num1 = int(input('Enter number: '))

if num1 > 0:
    print(f"{num1} is a positive number")

elif num1 < 0:
    print(f"{num1} is a negative number number")

elif num1 == 0:
    print(f"{num1} is equals to zero")

else:
    print("i don't know")

if num1 % 2 == 0 :
        print(f"{num1} is even number")

else:
        print(f"{num1} is odd number")

    #Задача 2

num_1st = int(input('Enter number: '))
num_2nd = int(input('Enter number: '))


if  num_2nd == 0:
     print('Invalid value')

elif num_1st % num_2nd == 0:
     result = num_1st % num_2nd
     print(f"{result} divides without remainder")

elif not num_1st % num_2nd == 0:
     result = num_1st % num_2nd
     print(f"{result} is the remainder")

else:
     print("this shouldn't have happened")