from interpreter.tokens import AVAILABLE_VARIABLE_CHARS, AVAILABLE_VARIABLE_PATTERN, FORBIDDEN_VARIABLE_NAMES, TokenType, Token
import re


class LexerException(Exception):
    pass


class Lexer():

    def __init__(self):
        self._pos: int = -1
        self._text: str = ''
        self._current_char: str = ''

    def next(self) -> Token:
        while self._current_char != None:
            if bool(re.match(r'[\t ]', self._current_char)):
                self._skip()
                continue
            
            if self._current_char == '\n':
                char = self._current_char
                self._forward()
                return Token(TokenType.EOL, char)
            if self._current_char == ':':
                char = self._assignment()
                return Token(TokenType.ASSIGN, char)
            if self._current_char.isdigit():
                token_type, value = self._number()
                return Token(token_type, value)
            if bool(re.match(AVAILABLE_VARIABLE_CHARS, self._current_char)):
                token_type, value = self._resolve_chars()
                return Token(token_type, value)
            if self._current_char == '+':
                char = self._current_char
                self._forward()
                return Token(TokenType.PLUS, char)
            if self._current_char == '-':
                char = self._current_char
                self._forward()
                return Token(TokenType.MINUS, char)
            if self._current_char == '*':
                char = self._current_char
                self._forward()
                return Token(TokenType.MUL, char)
            if self._current_char == '/':
                char = self._current_char
                self._forward()
                return Token(TokenType.DIV, char)
            if self._current_char == '(':
                char = self._current_char
                self._forward()
                return Token(TokenType.LPAREN, char)
            if self._current_char == ')':
                char = self._current_char
                self._forward()
                return Token(TokenType.RPAREN, char)
            if self._current_char == ';':
                char = self._current_char
                self._forward()
                return Token(TokenType.EOI, char)
            if self._current_char == '.':
                char = self._current_char
                self._forward()
                return Token(TokenType.EOP, char)
            raise LexerException(f"Bad token '{self._current_char}'!")
        return Token(TokenType.EOS, None)

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _skip(self):
        while bool(re.match(r'[\t ]', self._current_char)):
            self._forward()

    def _assignment(self) -> str:
        assignment_chars = [':', '=']
        result = ''
        while self._current_char in assignment_chars:
            result += self._current_char
            self._forward()
        
        if result == ':=':
            return result
        raise LexerException(f"Bad token '{result}'!")

    def _resolve_chars(self) -> str:
        result = ''
        while True:
            if bool(re.match(r'[\t ]', self._current_char)):
                break
            elif bool(re.match(AVAILABLE_VARIABLE_CHARS, self._current_char)):
                result += self._current_char
                self._forward()
            else:
                break

        if result.lower() in FORBIDDEN_VARIABLE_NAMES:
            if result.lower() == 'begin':
                return TokenType.SCOPE_START, result
            elif result.lower() == 'end':
                return TokenType.SCOPE_END, result
        elif bool(re.match(AVAILABLE_VARIABLE_PATTERN, result)):
            return TokenType.VAR, result
            
        raise LexerException(f"Bad token '{result}'!")

    def _number(self):
        result = []
        dots_amount = 0
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            if self._current_char == '.':
                dots_amount += 1
            if dots_amount > 1:
                raise LexerException("Invalid number!")
            result.append(str(self._current_char))
            self._forward()

        if result[len(result) - 1] == '.':
            raise LexerException("Invalid number!")
        if dots_amount > 0:
            token_type = TokenType.FLOAT
            value = float("".join(result))
        else:
            token_type = TokenType.INT
            value = int("".join(result))
        return token_type, value

    def init(self, text: str):
        self._text = text
        self._pos = -1
        self._forward()
