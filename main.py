from enum import Enum

def main():
    i = input('calculator>')
    accumulator = parse_input(i)
    while True:
        i = input('calculator> {:f} '.format(accumulator))
        accumulator = parse_input(i, accumulator, True)
def parse_input(string, accumulator = 0,  start_with_operator = False, ):
    parts = string.split(' ')
    current_operator = Operator.Add
    if start_with_operator:
        parts.insert(0, 0)
    for i, part in enumerate(parts):
        if i % 2 == 0:
            number = float(part)
            accumulator = perform_math(current_operator, accumulator, number)
        else:
            current_operator = convert(part)
    return accumulator
def perform_math(operator, accumulator, new_value):
    if operator == Operator.Add:
        return accumulator + new_value
    if operator == Operator.Subtract:
        return accumulator - new_value
    if operator == Operator.Multiply:
        return accumulator * new_value
    if operator == Operator.Divide:
        return accumulator / new_value
def convert(string):
    if string == '+':
        return Operator.Add
    if string == '-':
        return Operator.Subtract
    if string == '*':
        return Operator.Multiply
    if string == '/':
        return Operator.Divide
class Operator(Enum):
    Add = '+'
    Subtract = '-'
    Multiply = '*'
    Divide = '/'

if __name__ == '__main__':
    main()