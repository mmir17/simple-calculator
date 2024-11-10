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


user_input = input("Please enter the equation you would like to solve:")  # get equation
split_input = user_input.split  # split equation at every space

number = []
operation = []

for i in split_input:
    if split_input.index(i) % 2:  # if index evenly divisible by 2, then it's a number
        i = int(i)  # turn number into an integer
        number.append(i)  # append to the list of numbers
    else:
        operation.append(i)  # otherwise append to the list of operations

for i in number:    # iterate through the numbers
    for j in operation: # iterate through the operations
        n1 = i  # first number
        n2 = i + 1  # second number
        if j == "+":
            result = add(n1, n2)
        elif j == "-":
            result = subtract(n1, n2)
        elif j == "*":
            result = multiply(n1, n2)
        elif j == "/":
            result = divide(n1, n2)
        j += 1
    i += 2

print(result)  # print answer

