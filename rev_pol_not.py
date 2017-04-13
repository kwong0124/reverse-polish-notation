# import operator module
import operator

# make a function to evaluate the stack
def evaluate(*args):

    # determine the number of args
    num_args = len(args)
    # holds the numbrs in the stack
    stack = []
    # keeps a list of available inputs
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    operators = ['+', '-', '/', '*']

    for arg in args:
        if arg in numbers:
            stack.append(arg)
        elif arg in operators:
            # make a function to deal with operators - call from this function
            pass
        else:
            print('''
            Cannot read input. Please use only numbers zero through
            10 and the following operators for addition (+), subtraction (-),
            division (/) and multipliation (*)''')
            break


evaluate(5, 1, 2, '//', 4, 'x', '+', 3, '-')
