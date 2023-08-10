import unittest
import Befunge
import instructions
import Pointer


class InterpreterTest(unittest.TestCase):
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

    def test_floordiv(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.floordiv(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 0)

    def test_mod(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(5)
        interpreter.pointer.stack.append(7)
        instructions.mod(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 5)

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

    def test_step_up_or_down(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(0)
        instructions.step_up_or_down(interpreter)
        self.assertEqual(interpreter.pointer.vector, 'v')

    def test_step_left_or_right(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(0)
        instructions.step_left_or_right(interpreter)
        self.assertEqual(interpreter.pointer.vector, '>')

    def test_swap(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(0)
        interpreter.pointer.stack.append(50)
        instructions.swap(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 0)
        self.assertEqual(interpreter.pointer.stack.pop(), 50)

    def test_delete(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        interpreter.pointer.stack.append(1)
        interpreter.pointer.stack.append(2)
        interpreter.pointer.stack.append(555)
        instructions.delete(interpreter)
        self.assertEqual(interpreter.pointer.stack.pop(), 2)

    def test_right(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        instructions.right(interpreter)
        self.assertEqual(interpreter.pointer.vector, '>')

    def test_left(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        instructions.left(interpreter)
        self.assertEqual(interpreter.pointer.vector, '<')

    def test_up(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        instructions.up(interpreter)
        self.assertEqual(interpreter.pointer.vector, '^')

    def test_down(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        instructions.down(interpreter)
        self.assertEqual(interpreter.pointer.vector, 'v')

    def test_text(self):
        interpreter = Befunge.Interpreter('programs/Hello_world.txt')
        self.assertEqual(interpreter.text[1][0], '@')


if __name__ == '__main__':
    unittest.main()
