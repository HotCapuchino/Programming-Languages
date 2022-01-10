from typing import Union
import pytest
from interpreter import Interpreter
from interpreter.interpreter import InterpreterException
from interpreter.node import Node

@pytest.fixture
def testInterpreter():
    return Interpreter()

@pytest.fixture
def empty():
    f = open('./test_res/test1.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def wrapped() -> str:
    f = open('./test_res/test4.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def mathStatement() -> str:
    f = open('./test_res/test5.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def wrongUnOp() -> str:
    f = open('./test_res/test6.txt')
    text = f.read()
    f.close()
    return text


class TestInterpreter:

    def test_empty(self, testInterpreter: Interpreter):
        assert testInterpreter(None) == {}

    def test_empty_program(self, testInterpreter: Interpreter, empty):
        assert testInterpreter(empty) == {}

    def test_wrapped_statement(self, testInterpreter: Interpreter, wrapped: str):
        assert testInterpreter(wrapped) == {'x': 2.0, 'a': 3}

    def test_several_statements(self, testInterpreter: Interpreter, mathStatement: str):
        assert testInterpreter(mathStatement) == {'y': 2, 'x': -3.0}

    def test_wrong_unary_operation(self, testInterpreter: Interpreter, wrongUnOp: str):
        with pytest.raises(InterpreterException):
            testInterpreter(wrongUnOp)