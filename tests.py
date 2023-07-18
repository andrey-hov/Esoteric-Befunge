import unittest
import Befunge


class MyTestCase(unittest.TestCase):
    def test_Fibonachi(self):
        self.assertEqual(Befunge.Interpreter('programs/Fibonachi.txt').start(), '0 1 1 2 3 5 8 13 21 34 55 89 144 233 ')

    def test_HelloWorld(self):
        self.assertEqual(Befunge.Interpreter('programs/Hello_world.txt').start(), 'Hello World!')

    def test_random_number(self):
        self.assertIn(Befunge.Interpreter('programs/random_number.txt').start(), ['0', '1', '2', '3', '4', '5',
                                                                                  '6', '7', '8', '9'])

    def test_pointer(self):
        self.assertEqual(Befunge.Pointer('<').get(), '<')




if __name__ == '__main__':
    unittest.main()
