import Befunge
import argparse

parser = argparse.ArgumentParser(description='Befunge_interpreter')
parser.add_argument('file_path', type=str, help='The path to the executable file')
args = parser.parse_args()


if __name__ == '__main__':
    print(Befunge.Interpreter(args.file_path).start())
