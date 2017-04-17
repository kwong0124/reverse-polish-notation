import operator
from numbers import Number
from decimal import Decimal
from fractions import Fraction

# To-do list:
# -make it so that the program can accept other types of numbers
# -add a main function which prints the final answer
# -try additional test cases
# -check for incorrectly entered calculations
# -wrap code that is too long so that it goes onto another line
# - add functionality to take user input

# holds the numbrs in the stack
stack = []

# keeps a list of available inputs (numbers and operators)
numbers = list(range(100))
operators = ['+', '-', '/', '*']

print('''
    This program is a reverse polish notation calculator.
    The calculator can accept any whole number integers as well
    as opeators: +, -, *, /''')
print('''
    The rules for reverse polish notation calculation can be found at
    https://en.wikipedia.org/wiki/Reverse_Polish_notation''')

# make a function to evaluate the stack
def evaluate_input(calculation):
    '''Iterates through the args and determines whether each arg is
    a number, an operator or none of the above. If the arg is a number, it gets
    added to the stack, if the arg is an operator, the eval_ops function is
    called. If the arg is neither a number or an operator, the function will
    display an error message and end the program.'''

    # Split user inputs into a list separated by spaces
    num_ops = calculation.split(' ')

    for item in num_ops:
        try:
            stack.append(float(item))
            print(stack)
        except:
            print('This is not a number')


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

if __name__ == '__main__':
    # how to input both strings and ints?
    evaluate_input(input('Please enter numbers and operators separated by a space: '))
