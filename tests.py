import unittest
import Befunge
import instructions
import Pointer


class MyTestCase(unittest.TestCase):
    # def test_Fibonachi(self):
    #     self.assertEqual(Befunge.Interpreter('programs/Fibonachi.txt').start('go'),
    #                      '0 1 1 2 3 5 8 13 21 34 55 89 144 233 ')
    #
    # def test_HelloWorld(self):
    #     self.assertEqual(Befunge.Interpreter('programs/Hello_world.txt').start('go'),
    #                      'Hello World!')
    #
    # def test_random_number(self):
    #     self.assertIn(Befunge.Interpreter('programs/random_number.txt').start('go'),
    #                   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_pointer(self):
        self.assertEqual(Pointer.Pointer('<').get(), '<')

    def test_step(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.step()
        self.assertEqual(interpreter.pointer.x, 0)
        self.assertEqual(interpreter.pointer.y, 1)

    def test_add(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.add(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 12)

    def test_sub(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.sub(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), -2)

    def test_mul(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.mul(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 35)

    def test_random(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        instructions.random_vector(interpreter)
        self.assertIn(interpreter.pointer.vector, ['^', 'v', '>', '<'])

    def test_greater(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.greater(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 0)

    def test_negative(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(1)
        instructions.negative(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 0)

    def test_clear_stack(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(1)
        interpreter.pointer.stack.append(2)
        interpreter.pointer.stack.append(555)
        instructions.clear_stack(interpreter)
        self.assertEqual(len(interpreter.pointer.stack), 0)

    def test_double(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(1)
        instructions.double(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 1)
        self.assertEqual(interpreter.pointer.stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()
