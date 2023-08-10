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
        if (len(self.field) <= self.x or self.x < 0 or
                len(self.field[0]) <= self.y or self.y < 0):
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
