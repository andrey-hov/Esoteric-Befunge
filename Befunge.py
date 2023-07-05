import random


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
        pointer = self.pointer
        while True:
            e = pointer.get()
            if e == '>':
                pointer.vector = '>'
            elif e == '<':
                pointer.vector = '<'
            elif e == '^':
                pointer.vector = '^'
            elif e == 'v':
                pointer.vector = 'v'
            elif e.isdigit():
                pointer.stack.append(int(e))
            elif e == 'p':
                x = pointer.stack.pop()
                y = pointer.stack.pop()
                value = pointer.stack.pop()
                pointer.A[x][y] = chr(value)
            elif e == 'g':
                x = pointer.stack.pop()
                y = pointer.stack.pop()
                value = pointer.A[x][y]
                pointer.stack.append(ord(value))
            elif e == '|':
                flag = pointer.stack.pop()
                if flag == 0:
                    pointer.vector = 'v'
                else:
                    pointer.vector = '^'
            elif e == '_':
                flag = pointer.stack.pop()
                if flag == 0:
                    pointer.vector = '>'
                else:
                    pointer.vector = '<'
            elif e == '?':
                pointer.vector = random.choice(['^', 'v', '>', '<'])
            elif e in ['+', '-', '*', '/', '%']:
                b = pointer.stack.pop()
                a = pointer.stack.pop()
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
                pointer.stack.append(res)
            elif e == '\\':
                a = pointer.stack.pop()
                b = pointer.stack.pop()
                pointer.stack.append(a)
                pointer.stack.append(b)
            elif e == ':':
                a = pointer.stack.pop()
                pointer.stack.append(a)
                pointer.stack.append(a)
            elif e == ',':
                a = pointer.stack.pop().decode('ASCII')
                result += a
            elif e == '.':
                a = pointer.stack.pop()
                result += str(a)
            elif e == '$':
                pointer.stack.pop()
            elif e == '!':
                if pointer.stack.pop() == 0:
                    pointer.stack.append(1)
                else:
                    pointer.stack.append(0)
            elif e == '`':
                a = pointer.stack.pop()
                b = pointer.stack.pop()
                if b > a:
                    pointer.stack.append(1)
                else:
                    pointer.stack.append(0)
            elif e == '\"':
                pointer.step()
                e = pointer.get()
                while e != '\"':
                    pointer.stack.append(e.encode('ASCII'))
                    pointer.step()
                    e = pointer.get()
            elif e == '@':
                break
            pointer.step()
            if e == '#':
                pointer.step()
        return result
