import random
import sys


class Pointer:
    """
    Поинтер
    Принимает массив строк (поле)
    Отвечает за хождение по полю
    """

    def __init__(self, text):
        self.field = []
        self.x = 0
        self.y = 0
        self.vector = '>'
        self.stack = []
        self.init_field(text)

    def get(self):
        return self.field[self.x][self.y]

    def step(self):
        if self.vector == '>':
            self.y += 1
        elif self.vector == '<':
            self.y -= 1
        elif self.vector == '^':
            self.x -= 1
        elif self.vector == 'v':
            self.x += 1
        if len(self.field) <= self.x or self.x < 0 or len(self.field[0]) <= self.y or self.y < 0:
            sys.exit('Выход за пределы поля')

    def init_field(self, text):
        row = len(text)
        column = 0

        for line in text:
            if len(line) > column:
                column = len(line)

        self.field = [' '] * row
        for i in range(row):
            self.field[i] = [' '] * column

        for i in range(len(text)):
            for j in range(len(text[i])):
                self.field[i][j] = text[i][j]

    def field_print(self):
        for row in self.field:
            for elem in row:
                print(elem, end='')
            print()


class Interpreter:
    """
    Интерпретатор
    Принимает путь до файла и выполняет его.
    """

    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as f:
                text = f.read().split("\n")
        except:
            sys.exit("Ошибка открытия файла")
        self.pointer = Pointer(text)

    def add(self):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        return a + b

    def sub(self):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        return a - b

    def mul(self):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        return a * b

    def floordiv(self):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        if b == 0:
            return 0
        else:
            return a // b

    def mod(self):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        return a % b

    def random(self):
        self.pointer.vector = random.choice(['^', 'v', '>', '<'])

    def right(self):
        self.pointer.vector = '>'

    def left(self):
        self.pointer.vector = '<'

    def up(self):
        self.pointer.vector = '^'

    def down(self):
        self.pointer.vector = 'v'

    def delete(self):
        self.pointer.stack.pop()

    def print_number(self):
        a = self.pointer.stack.pop()
        print(str(a), end='')

    def print_symbol(self):
        a = self.pointer.stack.pop().decode('ASCII')
        print(a, end='')

    def greater(self):
        a = self.pointer.stack.pop()
        b = self.pointer.stack.pop()
        if b > a:
            self.pointer.stack.append(1)
        else:
            self.pointer.stack.append(0)

    def swap(self):
        a = self.pointer.stack.pop()
        try:
            b = self.pointer.stack.pop()
        except:
            b = 0
        self.pointer.stack.append(a)
        self.pointer.stack.append(b)

    def put(self):
        x = self.pointer.stack.pop()
        y = self.pointer.stack.pop()
        value = self.pointer.stack.pop()
        self.pointer.field[x][y] = chr(value)

    def get(self):
        x = self.pointer.stack.pop()
        y = self.pointer.stack.pop()
        value = self.pointer.field[x][y]
        self.pointer.stack.append(ord(value))

    def step_up_or_down(self):
        flag = self.pointer.stack.pop()
        if flag == 0:
            self.pointer.vector = 'v'
        else:
            self.pointer.vector = '^'

    def step_left_or_right(self):
        flag = self.pointer.stack.pop()
        if flag == 0:
            self.pointer.vector = '>'
        else:
            self.pointer.vector = '<'

    def put_symbol(self):
        self.pointer.stack.append(ord(input('Введите символ: ')[0]))

    def negative(self):
        if self.pointer.stack.pop() == 0:
            self.pointer.stack.append(1)
        else:
            self.pointer.stack.append(0)

    def next(self):
        self.pointer.step()

    def input_number(self):
        a = input('Введите число: ')
        if a.isdigit():
            self.pointer.stack.append(int(a))
        else:
            sys.exit('Это не число!')

    def string(self):
        self.pointer.step()
        e = self.pointer.get()
        while e != '\"':
            self.pointer.stack.append(e.encode('ASCII'))
            self.pointer.step()
            e = self.pointer.get()

    def double(self):
        a = self.pointer.stack.pop()
        self.pointer.stack.append(a)
        self.pointer.stack.append(a)

    def clear_stack(self):
        self.pointer.stack.clear()

    def jump_forward(self):
        a = self.pointer.stack.pop()
        for i in range(a):
            self.pointer.step()

    methods = {'+': add,
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
               '#': next,
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

    def start_go(self):
        while True:
            e = self.pointer.get()
            if e == '@':
                break
            if e.isdigit():
                self.pointer.stack.append(int(e))
            else:
                self.methods[e]()
            self.pointer.step()

    def start_steps(self):
        flag = 0
        while flag == 0:
            n = int(input('Введите количество шагов: '))
            for i in range(n):
                e = self.pointer.get()
                if e == '@':
                    flag = 1
                    break
                if e.isdigit():
                    self.pointer.stack.append(int(e))
                else:
                    self.methods[e]()
                self.pointer.step()

    def start(self, go_or_steps):
        if go_or_steps == 'go':
            self.start_go()
        elif go_or_steps == 'steps':
            self.start_steps()
