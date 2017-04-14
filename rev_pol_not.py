# import operator module
import operator

# To-do list:
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
    '''Iterates through the args and determines whether each arg is
    a number, an operator or none of the above. If the arg is a number, it gets
    added to the stack, if the arg is an operator, the eval_ops function is
    called. If the arg is neither a number or an operator, the function will
    display an error message and end the program.'''

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
    print(stack)

def eval_ops(symbol, a, b):
    '''The eval_ops function take three inputs - an operator (called symbol), an
    'a' argument and a 'b' argument, and performs the calculation implied by the
    operator. Operations are performed using the operator module. For example,
    if the operator is subtraction (-), a = 2 and b = 4, the function will
    calculate 2 - 4 = -2.'''

    # create a dict to map input operators to operator functions
    operator_dict = {'+': operator.add(a, b), '-': operator.sub(a, b), '*': operator.mul(a, b), '/': operator.truediv(a, b)}

    stack.append(operator_dict[symbol])

    #if symbol == '+':
    #    stack.append(operator.add(a, b))
    #if symbol == '*':
    #    stack.append(operator.mul(a, b))
    #if symbol == '-':
    #    stack.append(operator.sub(a, b))
    #if symbol == '/':
    #    stack.append(operator.truediv(a, b))

evaluate_input(7, 9, 1, '+', 4, '*', '+', 3, '-')
