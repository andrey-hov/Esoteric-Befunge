import Befunge
import argparse

parser = argparse.ArgumentParser(description='Befunge_interpreter')
parser.add_argument('file_path', type=str, help='The path to the executable file')
parser.add_argument('go_or_steps', type=str, help='Choice')
args = parser.parse_args()


if __name__ == '__main__':
    Befunge.Interpreter(args.file_path).start(args.go_or_steps)
