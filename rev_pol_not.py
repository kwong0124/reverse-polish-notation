# import operator module
import operator

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
            eval_ops(arg, a=stack[-2], b=stack[-1])
        else:
            print('''
            Cannot read {}. Please use only numbers zero through
            10 and the following operators for addition (+), subtraction (-),
            division (/) and multipliation (*)'''.format(arg))
            break

def eval_ops(symbol, a, b):
    #create a dict to map input operators to operator functions
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    print('operator = {}, a = {}, b = {}'.format(symbol, a, b))




evaluate_input(5, 1, 2, 4, '*', '+', 3, '-')
