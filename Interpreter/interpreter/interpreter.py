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

    def _factor(self) -> float:
        token = self._current_token
        print('factor', self._current_token.type_)
        if token.type_ == TokenType.FLOAT:
            self.check_token_type(TokenType.FLOAT)
            return float(token.value)
        if token.type_ == TokenType.LPAREN:
            self.check_token_type(TokenType.LPAREN)
            result = self._expression()
            self.check_token_type(TokenType.RPAREN)
            return result
        raise InterpreterException('Invalid factor!')

    def _term(self) -> float:
        result = self._factor()
        ops = [TokenType.DIV, TokenType.MUL]
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self.check_token_type(TokenType.MUL)
                result *= self._factor()
            elif token.type_ == TokenType.DIV:
                self.check_token_type(TokenType.DIV)
                result /= self._factor()
        return result

    def _expression(self) -> float:
        self._current_token = self._lexer.next()
        print('expression', self._current_token.type_)
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self.check_token_type(TokenType.PLUS)
                result += self._term()
                print(result)
            elif token.type_ == TokenType.MINUS:
                self.check_token_type(TokenType.MINUS)
                result -= self._term()
        return result

    def __call__(self, text: str) -> float:
        return self.interpret(text)

    def interpret(self, text: str) -> float:
        self._lexer.init(text)
        return self._expression()


class InterpreterException(Exception):
    pass
