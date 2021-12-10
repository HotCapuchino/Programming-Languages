from interpreter.lexer import Lexer
from interpreter.node import BinaryOperation, Node, Number, UnaryOperation
from interpreter.tokens import Token, TokenType


class Parser:
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def parse(self, text: str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._expr()

    def __call__(self, text: str) -> Node:
        return self.parse(text)

    def _factor(self) -> Node:
        token = self._current_token
        
        if token.type_ == TokenType.FLOAT:
            self._check_token_type(TokenType.FLOAT)
            return Number(token)
        elif token.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)
            return UnaryOperation(token, self._factor())
        elif token.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
            return UnaryOperation(token, self._factor())
        elif token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        else:
            raise ParserException(f"Invalid factor - {token.type_}")

    def _term(self) -> Node:
        result = self._factor()
        ops = [TokenType.MUL, TokenType.DIV]

        if self._current_token is None: return None
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinaryOperation(result, token, self._factor())
        return result

    def _expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()

        if self._current_token is None: return None
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)              
            result = BinaryOperation(result, token, self._term())
        return result

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise ParserException(f"Invalid expression - expected token type: {type_}")

class ParserException(Exception):
    pass
