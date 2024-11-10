# create functions for each operation
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print('error!')


# ask the user which operation they would like to perform
print('Here are the available operations:')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

opp = int(input('Please enter the number of the operation you would like to perform.\n'))

if opp == 1 or opp == 2 or opp == 3 or opp == 4:
    n1 = float(input('Please enter the first number:'))
    n2 = float(input('Please enter the second number:'))
    if opp == 1:
        print(add(n1, n2))
    elif opp == 2:
        print(subtract(n1, n2))
    elif opp == 3:
        print(multiply(n1, n2))
    elif opp == 4:
        print(divide(n1, n2))
else:
    print('error!')
