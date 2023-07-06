import sys
import Befunge


if __name__ == '__main__':
    for i in sys.stdin:
        if str(i).rstrip('\n') == 'Exit':
            print('Done')
            break
        print(Befunge.Interpreter(str(i).rstrip('\n')).start())
        break
