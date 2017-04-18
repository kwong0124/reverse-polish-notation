# Reverse polish notation calculator
import operator
import math

# holds the numbrs in the stack
stack = []

# Defines the operators that can be used
operators = ['+', '-', '/', '*']

print('''
    This program is a reverse polish notation calculator. The rules for reverse
    polish notation calculation can be found at
    https://en.wikipedia.org/wiki/Reverse_Polish_notation .
    You may enter any of the following operators, +, -, *, /, for use in your
    calculations. Enter calculations in reverse polish notation. Each value
    entered should be separated by space.
    ''')


def is_number(num):
    '''
    Determines whether each item in equation is a number using try and
    except block
    '''

    try:
        float(num)
        return True
    except ValueError:
        pass


def evaluate_input(arg):
    '''
    Iterates through each item in equation to check if it is a number. If
    is_number returns true, the float of the item is appended to the stack.
    Else, the eval_ops equation is called to perform calculations on the stack.
    '''

    for item in arg:
        if is_number(item):
            stack.append(float(item))
        else:
            eval_ops(symbol=item, a=stack.pop(-2), b=stack.pop(-1))


def eval_ops(symbol, a, b):
    '''
    The eval_ops function take three inputs - an operator (called symbol), an
    'a' argument and a 'b' argument, and performs the calculation implied by the
    operator. Operations are performed using the operator module. For example,
    if the operator is subtraction (-), a = 2 and b = 4, the function will
    calculate 2 - 4 = -2.
    '''

    operator_dict = {'+': operator.add(a, b), '-': operator.sub(a, b), '*': operator.mul(a, b), '/': operator.truediv(a, b)}

    stack.append(operator_dict[symbol])


def main():
    equation = input('Enter the function you would like to calculate with a space between each value: ').split()
    answer = evaluate_input(equation)
    print('answer is: {}'.format(stack))
    

if __name__ == '__main__':
    # how to input both strings and ints?
    main()
