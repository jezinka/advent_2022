import re

from main.aoc_21a import prepare_monkeys, SIGN_REGEXP

opposite_ops = {'+': '-',
                '-': '+',
                '*': '/',
                '/': '*'}


def get_result(file_name):
    cpu, monkeys = prepare_monkeys(file_name)

    m1, m2 = [m.strip() for m in re.split(SIGN_REGEXP, monkeys['root'])]
    operation2 = get_value(m2, monkeys, cpu)
    operation1 = get_value(m1, monkeys, cpu)

    while operation1 != 'x':
        operation1, operation2 = left_brackets(operation1, operation2)

    return operation2


def left_brackets(operation1, operation2):
    operation1 = operation1[1:-1]
    left_index, right_index = find_brackets_index(operation1)
    left_overs = operation1[0:left_index] + operation1[right_index + 1:]
    if left_overs[0] in ['+', '-', '*', '/']:
        op = left_overs[0]
        rest = left_overs.removeprefix(op)
        operation = f'{operation2}{opposite_ops[op]}{eval(rest)}'
    else:
        op = left_overs[-1]
        rest = left_overs.removesuffix(op)
        if op == '/':
            operation = f'{eval(rest)}{op}{operation2}'
        elif op == '-':
            operation = f'-{operation2}{opposite_ops[op]}{eval(rest)}'
        else:
            operation = f'{operation2}{opposite_ops[op]}{eval(rest)}'
    operation2 = eval(operation)
    operation1 = operation1[left_index:right_index + 1]
    return operation1, operation2


def find_brackets_index(operation1):
    number_of_brackets = sum([1 for n in operation1[:operation1.index('x')] if n == '('])
    left_index = operation1.index('x')
    right_index = operation1.index('x')
    i = 0
    while i < number_of_brackets:

        left_founded = False
        right_founded = False

        while not left_founded:
            left_index -= 1
            if operation1[left_index] == '(':
                left_founded = True

        while not right_founded:
            right_index += 1
            if operation1[right_index] == ')':
                right_founded = True
        i += 1
    return left_index, right_index


def get_value(name, monkeys, cpu):
    if name == 'humn':
        return 'x'

    if name in cpu.keys():
        return str(cpu[name])

    op = monkeys[name]
    op_sign = re.search(f'({SIGN_REGEXP})', op).group(1)
    monkey_1, monkey_2 = [m.strip() for m in re.split(SIGN_REGEXP, op)]

    operation = f'({get_value(monkey_1, monkeys, cpu)}{op_sign}{get_value(monkey_2, monkeys, cpu)})'

    if 'x' in operation:
        return operation

    return str(eval(operation))


if __name__ == '__main__':
    assert get_result('test_data/21') == 301
    print(get_result('data/21'))
