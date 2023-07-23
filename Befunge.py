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
            raise Exception('Выход за пределы поля')

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

    def arithmetic(self, e):
        b = self.pointer.stack.pop()
        a = self.pointer.stack.pop()
        if e == '+':
            return a + b
        elif e == '-':
            return a - b
        elif e == '*':
            return a * b
        elif e == '/':
            if b == 0:
                return 0
            else:
                return a // b
        elif e == '%':
            return a % b

    def choice_vector(self, e):
        flag = self.pointer.stack.pop()
        if flag == 0:
            if e == '|':
                return 'v'
            else:
                return '>'
        else:
            if e == '|':
                return '^'
            else:
                return '<'

    def start(self):
        result = ''
        point = self.pointer
        while True:
            e = point.get()
            if e in ['>', '<', '^', 'v']:
                point.vector = e
            elif e.isdigit():
                point.stack.append(int(e))
            elif e == 'p':
                x = point.stack.pop()
                y = point.stack.pop()
                value = point.stack.pop()
                point.field[x][y] = chr(value)
            elif e == 'g':
                x = point.stack.pop()
                y = point.stack.pop()
                value = point.field[x][y]
                point.stack.append(ord(value))
            elif e == '|':
                point.vector = self.choice_vector(e)
            elif e == '_':
                point.vector = self.choice_vector(e)
            elif e == '?':
                point.vector = random.choice(['^', 'v', '>', '<'])
            elif e in ['+', '-', '*', '/', '%']:
                point.stack.append(self.arithmetic(e))
            elif e == '\\':
                a = point.stack.pop()
                try:
                    b = point.stack.pop()
                except:
                    b = 0
                point.stack.append(a)
                point.stack.append(b)
            elif e == ':':
                a = point.stack.pop()
                point.stack.append(a)
                point.stack.append(a)
            elif e == ',':
                a = point.stack.pop().decode('ASCII')
                result += a
            elif e == '.':
                a = point.stack.pop()
                result += str(a)
            elif e == '$':
                point.stack.pop()
            elif e == '&':
                a = input('Введите число: ')
                if a.isdigit():
                    point.stack.append(int(a))
                else:
                    raise Exception('Это не число')
            elif e == '#':
                point.step()
            elif e == '~':
                point.stack.append(ord(input('Введите символ: ')[0]))
            elif e == '!':
                if point.stack.pop() == 0:
                    point.stack.append(1)
                else:
                    point.stack.append(0)
            elif e == '`':
                a = point.stack.pop()
                b = point.stack.pop()
                if b > a:
                    point.stack.append(1)
                else:
                    point.stack.append(0)
            elif e == '\"':
                point.step()
                e = point.get()
                while e != '\"':
                    point.stack.append(e.encode('ASCII'))
                    point.step()
                    e = point.get()
            elif e == '@':
                break
            point.step()
        return result
