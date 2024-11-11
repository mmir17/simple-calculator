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


#   take user input
user_input = input("Please enter the equation you would like to solve: ")  # get equation
split_input = enumerate(user_input.split())  # split equation at every space
#   give index and value for each split part

number = []
operation = []

#   separate the numbers vs operations
for i, num in split_input:
    if i % 2 == 0:  # if index evenly divisible by 2, then it's a number
        num = int(num)  # turn number into an integer
        number.append(num)  # append to the list of numbers
    else:
        operation.append(num)  # otherwise append to the list of operations

#   calculate
n1 = number[0]  # first number
for i in range(len(operation)):  # iterate through the operations
    n2 = number[i + 1]  # second number
    opp = operation[i]  # current operation
    if opp == "+":
        n1 = add(n1, n2)
    elif opp == "-":
        n1 = subtract(n1, n2)
    elif opp == "*":
        n1 = multiply(n1, n2)
    elif opp == "/":
        n1 = divide(n1, n2)

print(n1)  # print answer
