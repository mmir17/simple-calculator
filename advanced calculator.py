# create the functions for the operations:

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


user_input = input("Please enter the equation you would like to solve:")