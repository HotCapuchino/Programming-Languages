from interpreter import Interpreter
from interpreter import Parser

if __name__ == '__main__':
    parser = Parser()
    my_interpreter = Interpreter()
    program_text = open('./test_res/test5.txt').read()
    syntax_tree = parser(program_text)
    print(my_interpreter(syntax_tree))