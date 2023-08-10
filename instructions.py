import random
import sys


def add(interpreter):
    b = interpreter.pointer.stack.pop()
    a = interpreter.pointer.stack.pop()
    interpreter.pointer.stack.append(a + b)


def sub(interpreter):
    b = interpreter.pointer.stack.pop()
    a = interpreter.pointer.stack.pop()
    interpreter.pointer.stack.append(a - b)


def mul(interpreter):
    b = interpreter.pointer.stack.pop()
    a = interpreter.pointer.stack.pop()
    interpreter.pointer.stack.append(a * b)


def floordiv(interpreter):
    b = interpreter.pointer.stack.pop()
    a = interpreter.pointer.stack.pop()
    if b == 0:
        interpreter.pointer.stack.append(0)
    else:
        interpreter.pointer.stack.append(a // b)


def mod(interpreter):
    b = interpreter.pointer.stack.pop()
    a = interpreter.pointer.stack.pop()
    interpreter.pointer.stack.append(a % b)


def random_vector(interpreter):
    interpreter.pointer.vector = random.choice(['^', 'v', '>', '<'])


def right(interpreter):
    interpreter.pointer.vector = '>'


def left(interpreter):
    interpreter.pointer.vector = '<'


def up(interpreter):
    interpreter.pointer.vector = '^'


def down(interpreter):
    interpreter.pointer.vector = 'v'


def delete(interpreter):
    interpreter.pointer.stack.pop()


def print_number(interpreter):
    a = interpreter.pointer.stack.pop()
    print(str(a), end='')


def print_symbol(interpreter):
    a = interpreter.pointer.stack.pop().decode('ASCII')
    print(a, end='')


def greater(interpreter):
    a = interpreter.pointer.stack.pop()
    b = interpreter.pointer.stack.pop()
    if b > a:
        interpreter.pointer.stack.append(1)
    else:
        interpreter.pointer.stack.append(0)


def swap(interpreter):
    a = interpreter.pointer.stack.pop()
    try:
        b = interpreter.pointer.stack.pop()
    except IndexError:
        b = 0
    interpreter.pointer.stack.append(a)
    interpreter.pointer.stack.append(b)


def put(interpreter):
    x = interpreter.pointer.stack.pop()
    y = interpreter.pointer.stack.pop()
    value = interpreter.pointer.stack.pop()
    interpreter.pointer.field[x][y] = chr(value)


def get(interpreter):
    x = interpreter.pointer.stack.pop()
    y = interpreter.pointer.stack.pop()
    value = interpreter.pointer.field[x][y]
    interpreter.pointer.stack.append(ord(value))


def step_up_or_down(interpreter):
    flag = interpreter.pointer.stack.pop()
    if flag == 0:
        interpreter.pointer.vector = 'v'
    else:
        interpreter.pointer.vector = '^'


def step_left_or_right(interpreter):
    flag = interpreter.pointer.stack.pop()
    if flag == 0:
        interpreter.pointer.vector = '>'
    else:
        interpreter.pointer.vector = '<'


def put_symbol(interpreter):
    interpreter.pointer.stack.append(ord(input('Введите символ: ')[0]))


def negative(interpreter):
    if interpreter.pointer.stack.pop() == 0:
        interpreter.pointer.stack.append(1)
    else:
        interpreter.pointer.stack.append(0)


def next_point(interpreter):
    interpreter.pointer.step()


def input_number(interpreter):
    a = input('Введите число: ')
    if a.isdigit():
        interpreter.pointer.stack.append(int(a))
    else:
        sys.exit('Это не число!')


def string(interpreter):
    interpreter.pointer.step()
    e = interpreter.pointer.get()
    while e != '\"':
        interpreter.pointer.stack.append(e.encode('ASCII'))
        interpreter.pointer.step()
        e = interpreter.pointer.get()


def double(interpreter):
    a = interpreter.pointer.stack.pop()
    interpreter.pointer.stack.append(a)
    interpreter.pointer.stack.append(a)


def clear_stack(interpreter):
    interpreter.pointer.stack.clear()


def jump_forward(interpreter):
    a = interpreter.pointer.stack.pop()
    for i in range(a):
        interpreter.pointer.step()


def skip(interpreter):
    pass


methods = {' ': skip,
           '+': add,
           '-': sub,
           '/': floordiv,
           '*': mul,
           '%': mod,
           '?': random,
           '>': right,
           '<': left,
           '^': up,
           'v': down,
           '.': print_number,
           '\\': swap,
           '$': delete,
           '`': greater,
           'p': put,
           'g': get,
           '|': step_up_or_down,
           '_': step_left_or_right,
           '!': negative,
           '~': put_symbol,
           '#': next_point,
           ',': print_symbol,
           '&': input_number,
           '\"': string,
           ':': double,
           '(': double,
           ')': double,
           ';': double,
           '=': double,
           '[': double,
           ']': double,
           'h': double,
           'j': jump_forward,
           'n': clear_stack,
           '\'': double}
