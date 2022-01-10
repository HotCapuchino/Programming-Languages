from interpreter.node import BinaryOperation, MultiOperation, Node, Number, UnaryOperation, Variable
from interpreter.tokens import Token, TokenType


class TestNodes:
    
    def test_number_inequality(self):
        assert Number(Token(TokenType.INT, 4), TokenType.INT) != Node()

    def test_variable_inequality(self):
        assert Variable(Token(TokenType.VAR, 'x')) != Node()

    def test_binop_inequality(self):
        assert BinaryOperation(
            Number(Token(TokenType.INT, 4), TokenType.INT),
            Token(TokenType.MINUS, '-'),
            Number(Token(TokenType.INT, 4), TokenType.INT)
        ) != Node()

    def test_unop_inequality(self):
        assert UnaryOperation(
            Token(TokenType.MINUS, '-'),
            Number(Token(TokenType.INT, 4), TokenType.INT)
        ) != Node()

    def test_multi_inequality(self):
        assert MultiOperation([
            UnaryOperation(
                Token(TokenType.MINUS, '-'),
                Number(Token(TokenType.INT, 4), TokenType.INT)
            )   
        ]) != Node()

    def test_tokens_inequality(self):
        assert Token(TokenType.MINUS, '-') != Node()