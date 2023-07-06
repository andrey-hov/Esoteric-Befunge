import random
import sys


class Pointer:
    def __init__(self, file_name):
        self.A = []
        self.x = 0
        self.y = 0
        self.vector = '>'
        self.stack = []
        self.init_field(file_name)

    def get(self):
        return self.A[self.x][self.y]

    def step(self):
        if self.vector == '>':
            self.y += 1
        elif self.vector == '<':
            self.y -= 1
        elif self.vector == '^':
            self.x -= 1
        elif self.vector == 'v':
            self.x += 1
        if len(self.A[0]) <= self.x < 0 or len(self.A) <= self.y < 0:
            raise Exception('Выход за пределы поля')

    def init_field(self, file_name):
        with open(file_name, 'r') as f:
            text = f.read().split("\n")
        row = len(text)
        column = 0

        for line in text:
            if len(line) > column:
                column = len(line)

        self.A = [' '] * row
        for i in range(row):
            self.A[i] = [' '] * column

        for i in range(len(text)):
            for j in range(len(text[i])):
                self.A[i][j] = text[i][j]

    def field_print(self):
        for row in self.A:
            for elem in row:
                print(elem, end='')
            print()


class Interpreter:
    def __init__(self, file_name):
        self.pointer = Pointer(file_name)

    def start(self):
        result = ''
        p = self.pointer
        while True:
            e = p.get()
            if e == '>':
                p.vector = '>'
            elif e == '<':
                p.vector = '<'
            elif e == '^':
                p.vector = '^'
            elif e == 'v':
                p.vector = 'v'
            elif e.isdigit():
                p.stack.append(int(e))
            elif e == 'p':
                x = p.stack.pop()
                y = p.stack.pop()
                value = p.stack.pop()
                p.A[x][y] = chr(value)
            elif e == 'g':
                x = p.stack.pop()
                y = p.stack.pop()
                value = p.A[x][y]
                p.stack.append(ord(value))
            elif e == '|':
                flag = p.stack.pop()
                if flag == 0:
                    p.vector = 'v'
                else:
                    p.vector = '^'
            elif e == '_':
                flag = p.stack.pop()
                if flag == 0:
                    p.vector = '>'
                else:
                    p.vector = '<'
            elif e == '?':
                p.vector = random.choice(['^', 'v', '>', '<'])
            elif e in ['+', '-', '*', '/', '%']:
                b = p.stack.pop()
                a = p.stack.pop()
                if e == '+':
                    res = a + b
                elif e == '-':
                    res = a - b
                elif e == '*':
                    res = a * b
                elif e == '/':
                    if b == 0:
                        res = 0
                    else:
                        res = a // b
                elif e == '%':
                    res = a % b
                p.stack.append(res)
            elif e == '\\':
                a = p.stack.pop()
                try:
                    b = p.stack.pop()
                except:
                    b = 0
                p.stack.append(a)
                p.stack.append(b)
            elif e == ':':
                a = p.stack.pop()
                p.stack.append(a)
                p.stack.append(a)
            elif e == ',':
                a = chr(p.stack.pop())
                result += a
            elif e == '.':
                a = p.stack.pop()
                result += str(a)
            elif e == '$':
                p.stack.pop()
            elif e == '&':
                p.stack.append(int(input('Введите число: ')))
            elif e == '#':
                p.step()
            elif e == '~':
                p.stack.append(ord(input('Введите символ: ')[0]))
            elif e == '!':
                if p.stack.pop() == 0:
                    p.stack.append(1)
                else:
                    p.stack.append(0)
            elif e == '`':
                a = p.stack.pop()
                b = p.stack.pop()
                if b > a:
                    p.stack.append(1)
                else:
                    p.stack.append(0)
            elif e == '\"':
                p.step()
                e = p.get()
                while e != '\"':
                    p.stack.append(e.encode('ASCII'))
                    p.step()
                    e = p.get()
            elif e == '@':
                break
            p.step()
        return result
