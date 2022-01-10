from re import L
from typing import Union
import pytest
from interpreter import Parser, ParserException
from interpreter.node import BinaryOperation, MultiOperation, Node, Number, UnaryOperation, Variable
from interpreter.tokens import Token, TokenType

@pytest.fixture
def testParser() -> Parser:
    return Parser()

@pytest.fixture
def emptyProgram():
    f = open('./test_res/test1.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def simpleProgram1() -> Union[str, Node]:
    f = open('./test_res/test2.txt')
    text = f.read()
    f.close()

    syntax_tree = MultiOperation(
        [BinaryOperation(
            Number(Token(TokenType.INT, 2), TokenType.INT), 
            Token(TokenType.ASSIGN, ':='),
            Variable(Token(TokenType.VAR, 'x'))
        )]
    )
    return text, syntax_tree

@pytest.fixture
def simpleWrong() -> str:
    f = open('./test_res/test3.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def wrapped() -> Union[str, Node]:
    f = open('./test_res/test4.txt')
    text = f.read()
    f.close()

    syntax_tree = MultiOperation([
        BinaryOperation(
            Number(Token(TokenType.FLOAT, 2.0), TokenType.FLOAT), 
            Token(TokenType.ASSIGN, ':='),
            Variable(Token(TokenType.VAR, 'x'))),
        MultiOperation([
                BinaryOperation(
                    Number(Token(TokenType.INT, 3), TokenType.INT), 
                    Token(TokenType.ASSIGN, ':='),
                    Variable(Token(TokenType.VAR, 'a')))
        ])
    ])
    return text, syntax_tree

@pytest.fixture
def mathStatement() -> Union[str, Node]:
    f = open('./test_res/test5.txt')
    text = f.read()
    f.close()

    syntax_tree = MultiOperation([
        BinaryOperation(
             Number(Token(TokenType.INT, 2), TokenType.INT),
            Token(TokenType.ASSIGN, ':='),
            Variable(Token(TokenType.VAR, 'y'))
        ),
        BinaryOperation(
            BinaryOperation(
                BinaryOperation(
                    UnaryOperation(
                        Token(TokenType.MINUS, '-'), 
                        Number(Token(TokenType.INT, 2), TokenType.INT)
                    ),
                    Token(TokenType.MUL, '*'), 
                    BinaryOperation(
                        BinaryOperation(
                            Number(Token(TokenType.INT, 8), TokenType.INT), 
                            Token(TokenType.PLUS, '+'),
                            Number(Token(TokenType.INT, 3), TokenType.INT)
                        ), 
                        Token(TokenType.MINUS, '-'), 
                        Number(Token(TokenType.INT, 1), TokenType.INT)
                    )
                ),
                Token(TokenType.DIV, '/'),
                UnaryOperation(
                    Token(TokenType.PLUS, '+'), 
                    Number(Token(TokenType.INT, 4), TokenType.INT)
                ),
            ), 
            Token(TokenType.ASSIGN, ':='),
            Variable(Token(TokenType.VAR, 'x'))
        ), 
        BinaryOperation(
            BinaryOperation(
                Variable(Token(TokenType.VAR, 'x')),
                Token(TokenType.PLUS, '+'),
                Variable(Token(TokenType.VAR, 'y'))
            ),
            Token(TokenType.ASSIGN, ':='),
            Variable(Token(TokenType.VAR, 'x')) 
        )
    ])
    return text, syntax_tree

class TestParser:

    def test_empty_scope(self, testParser: Parser, emptyProgram: str):
        assert isinstance(testParser.parse(emptyProgram), Node)

    def test_call(self, testParser: Parser, emptyProgram: str): 
        assert isinstance(testParser(emptyProgram), Node)

    def test_simple_program(self, testParser: Parser, simpleProgram1: Union[str, Node]):
        program, syntax_tree = simpleProgram1
        assert testParser(program) == syntax_tree
    
    def test_simple_program_without_semi(self, testParser: Parser, simpleProgram1: Union[str, Node]):
        program, syntax_tree = simpleProgram1
        program = program.replace(';', '')
        assert testParser(program) == syntax_tree

    def test_wrong_program_without_semi(self, testParser: Parser, simpleWrong: str):
        with pytest.raises(ParserException):
            testParser(simpleWrong)

    def test_wrapped_program(self, testParser: Parser, wrapped: Union[str, Node]):
        program, syntax_tree = wrapped
        assert testParser(program) == syntax_tree

    def test_math_statement(self, testParser: Parser, mathStatement: Union[str, Node]):
        program, syntax_tree = mathStatement
        assert testParser(program) == syntax_tree

    def test_wrong_math_statement(self, testParser: Parser, mathStatement: Union[str, Node]):
        program, _ = mathStatement
        program = program.replace('BEGIN', 'END')
        with pytest.raises(ParserException):
            testParser(program)