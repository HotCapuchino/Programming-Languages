from interpreter.tokens import TokenType, Token


class Interpreter:

    def __init__(self):
        self._pos: int = -1
        self._current_token: Token = None
        self._text: str = ''
        self._current_char = ''

    def _next_token(self) -> Token:
        while self._current_char != None:
            if self._current_char == ' ':
                self._skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.INTEGER, self._integer())
            if self._current_char == '+':
                char = self._current_char
                self._forward()
                return Token(TokenType.PLUS, char)
            if self._current_char == '-':
                char = self._current_char
                self._forward()
                return Token(TokenType.MINUS, char)
            raise InterpreterException(f"bad token '{self._current_char}'!")

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _skip(self):
        while self._current_char == ' ':
            self._forward()

    def _integer(self) -> str:
        result = []
        while self._current_char and self._current_char.isdigit():
            result.append(str(self._current_char))
            self._forward()
        return "".join(result)

    def check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._next_token()
        else:
            raise InterpreterException("bad token order!")

    def _expression(self) -> int:
        self._current_token = self._next_token()
        left = self._current_token
        self.check_token_type(TokenType.INTEGER)
        op = self._current_token
        if op.type_ == TokenType.PLUS:
            self.check_token_type(TokenType.PLUS)
        elif op.type_ == TokenType.MINUS:
            self.check_token_type(TokenType.MINUS)
        right = self._current_token
        self.check_token_type(TokenType.INTEGER)
        if op.type_ == TokenType.PLUS:
            return int(left.value) + int(right.value)
        elif op.type_ == TokenType.MINUS:
            return int(left.value) - int(right.value)
        else:
            raise InterpreterException("unknown operator!")

    def __call__(self, text: str) -> int:
        return self.interpret(text)

    def interpret(self, text: str) -> int:
        self._text = text
        self._pos = -1
        self._forward()
        return self._expression()


class InterpreterException(Exception):
    pass