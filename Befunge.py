import sys
import instructions
import Pointer


class Interpreter:
    """
    Интерпретатор
    Принимает путь до файла и выполняет его.
    """

    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self.text = f.read().split("\n")
        except FileNotFoundError:
            sys.exit("Ошибка открытия файла")
        self.pointer = Pointer.Pointer(self.text)

    def start_go(self):
        while True:
            e = self.pointer.get()
            if e not in instructions.methods.keys():
                sys.exit(f'Несуществующий символ в программе: {e}')
            if e == '@':
                break
            if e.isdigit():
                self.pointer.stack.append(int(e))
            else:
                instructions.methods[e](self)
            self.pointer.step()

    def start_steps(self):
        flag = 0
        while flag == 0:
            print()
            n = int(input('Введите количество шагов: '))
            for i in range(n):
                e = self.pointer.get()
                if e not in instructions.methods.keys():
                    sys.exit(f'Несуществующий символ в программе: {e}')
                if e == '@':
                    flag = 1
                    break
                if e.isdigit():
                    self.pointer.stack.append(int(e))
                else:
                    instructions.methods[e](self)
                self.pointer.step()

    def start(self, go_or_steps):
        if go_or_steps == 'go':
            self.start_go()
        elif go_or_steps == 'steps':
            self.start_steps()
