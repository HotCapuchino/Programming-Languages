from HashMap.ModifiedDictErrors import InvalidDigitIndexException, InvalidMathSignException
from HashMap.Parser.tokens import AVAILABLE_MATH_SIGNS, Token, TokenType


class Lexer:
    
    def __init__(self):
        self._pos: int = -1
        self._text: str = ''
        self._current_char: str = ''

    def next(self) -> Token:
        while self._current_char != None:
            if self._current_char == ' ':
                self._skip()
                continue

            if self._current_char.isdigit():
                type, num = self._number()
                if type == int:
                    return Token(TokenType.INTEGER, num)
                else:
                    return Token(TokenType.FLOAT, num)

            if self._current_char == ',':
                char = self._current_char
                self._forward()
                return Token(TokenType.COMMA, char)

            if self._current_char in AVAILABLE_MATH_SIGNS:
                tokenType, value = self._define_math_sign()
                self._forward()
                return Token(tokenType, value)
                
        return Token(TokenType.EOS, None)

    def _number(self) -> tuple:
        number = ''
        dots_amount = 0
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            if dots_amount > 0:
                raise InvalidDigitIndexException('Invalid number! number of type int or float was expected!')
            number += str(self._current_char)
            if self._current_char == '.':
                dots_amount += 1
            self._forward()
        type = int
        if dots_amount > 0:
            type = float
        return type, number

    def _define_math_sign(self) -> tuple:
        math_sign = ''
        while self._current_char and self._current_char in AVAILABLE_MATH_SIGNS:
            math_sign += self._current_char
        if math_sign == '<':
            return TokenType.LESS, math_sign
        if math_sign == '>':
            return TokenType.GREATER, math_sign
        if math_sign == '=':
            return TokenType.EQUAL, math_sign
        if math_sign == '<=':
            return TokenType.LESS_OR_EQUAL, math_sign
        if math_sign == '>=':
            return TokenType.GREATER_OR_EQUAL, math_sign
        if math_sign == '<>':
            return TokenType.NOT_EQUAL, math_sign
        raise InvalidMathSignException('Invalid Math Sign!')

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _skip(self):
        while self._current_char == ' ':
            self._forward()