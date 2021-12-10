from interpreter import Interpreter
from interpreter import Parser

if __name__ == '__main__':
    parser = Parser()
    my_interpreter = Interpreter()
    syntax_tree = parser('-2 + -2')
    # print(syntax_tree)
    print(my_interpreter(syntax_tree))