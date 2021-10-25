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
                return Token(TokenType.FLOAT, self._number())
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

    def _number(self) -> str:
        result = []
        dots_amount = 0
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            if self._current_char == '.':
                dots_amount += 1
            if dots_amount > 1:
                raise InterpreterException("invalid number!")
            result.append(str(self._current_char))
            self._forward()
        if result[len(result) - 1] == '.':
            raise InterpreterException("invalid number!")
        return "".join(result)

    def check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._next_token()
        else:
            raise InterpreterException("bad token order!")

    def _expression(self) -> float:
        self._current_token = self._next_token()
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
        self._text = text
        self._pos = -1
        self._forward()
        return self._expression()


class InterpreterException(Exception):
    pass