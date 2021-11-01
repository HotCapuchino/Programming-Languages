from interpreter.lexer import Lexer
from interpreter.tokens import TokenType, Token


class Interpreter:

    def __init__(self):
        self._current_token: Token = None
        self._lexer = Lexer()

    def check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise InterpreterException("bad token order!")

    def _expression(self) -> float:
        self._current_token = self._lexer.next()
        left = self._current_token
        self.check_token_type(TokenType.FLOAT)
        op = self._current_token
        if op.type_ == TokenType.PLUS:
            self.check_token_type(TokenType.PLUS)
        elif op.type_ == TokenType.MINUS:
            self.check_token_type(TokenType.MINUS)
        right = self._current_token
        self.check_token_type(TokenType.FLOAT)
        if op.type_ == TokenType.PLUS:
            return float(left.value) + float(right.value)
        elif op.type_ == TokenType.MINUS:
            return float(left.value) - float(right.value)
        else:
            raise InterpreterException("unknown operator!")

    def __call__(self, text: str) -> float:
        return self.interpret(text)

    def interpret(self, text: str) -> float:
        self._lexer.init(text)
        return self._expression()


class InterpreterException(Exception):
    pass