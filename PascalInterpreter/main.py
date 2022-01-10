from interpreter import Interpreter

if __name__ == '__main__':
    my_interpreter = Interpreter()
    program_text = open('./res/test1.txt').read()
    print(my_interpreter(program_text))