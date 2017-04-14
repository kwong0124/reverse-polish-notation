# import operator module
import operator

# To-do list:
# -add doc strings and better documentation
# -add dictionary lookup for operators instead of if statements
# -make it so that the program can accept other types of numbers
# -add a main function which prints the final answer
# -try additional test cases

# holds the numbrs in the stack
stack = []

# keeps a list of available inputs (numbers and operators)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['+', '-', '/', '*']

# make a function to evaluate the stack
def evaluate_input(*args):

    for arg in args:
        if arg in numbers:
            stack.append(arg)

        elif arg in operators:
            # call function that deals with numerical operations
            eval_ops(symbol=arg, a=stack.pop(-2), b=stack.pop(-1))
        # if none of the above conditions apply, tell the user to change input
        else:
            print('''
            Cannot read {}. Please use only numbers zero through
            10 and the following operators for addition (+), subtraction (-),
            division (/) and multipliation (*)'''.format(arg))
            break
    return stack

def eval_ops(symbol, a, b):
    # create a dict to map input operators to operator functions
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if symbol == '+':
        stack.append(operator.add(a, b))
    if symbol == '*':
        stack.append(operator.mul(a, b))
    if symbol == '-':
        stack.append(operator.sub(a, b))
    if symbol == '/':
        stack.append(operator.truediv(a, b))

evaluate_input(5, 1, 2, '+', 4, '*', '+', 3, '-')
