# create the functions for the operations:

# function for adding two values together
def add(x, y):
    return x + y


# function for subtracting two values
def subtract(x, y):
    return x - y


# function for multiplying two values
def multiply(x, y):
    return x * y


# function for dividing two values
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print('error!')  # condition for dividing by zero


user_input = input("Please enter the equation you would like to solve:")
