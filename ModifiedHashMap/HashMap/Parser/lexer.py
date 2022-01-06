from ..ModifiedDictErrors import InvalidDigitIndexException, InvalidMathSignException, LexerException
from .tokens import MATH_SIGNS, Token, TokenCategory, TokenType


class Lexer:
    
    def __init__(self):
        self._pos: int = -1
        self._text: str = ''
        self._current_char: str = ''
        self._available_math_signs = [item.value for item in MATH_SIGNS]

    def init(self, text: str):
        self._text = text
        self._pos = -1
        self._forward()

    def next(self) -> Token:
        while self._current_char != None:
            if self._current_char == ' ':
                self._skip()
                continue

            if self._current_char.isdigit():
                type, num = self._number()
                if type == int:
                    return Token(TokenType.INTEGER, num, TokenCategory.DIGIT)
                else:
                    return Token(TokenType.FLOAT, num, TokenCategory.DIGIT)

            if self._current_char == ',':
                char = self._current_char
                self._forward()
                return Token(TokenType.COMMA, char, TokenCategory.DIVIDER)

            if self._current_char in self._available_math_signs:
                tokenType, value = self._define_math_sign()
                return Token(tokenType, value, TokenCategory.CONDITION)

            raise LexerException('Your condition doesn\'t match the pattern: (CONDITION, NUMBER, DELIMITER)!')
                
        return Token(TokenType.EOS, None, Token)

    def _number(self) -> tuple:
        number = ''
        dots_amount = 0
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            number += str(self._current_char)
            if self._current_char == '.':
                dots_amount += 1
            self._forward()
        if dots_amount > 0:
            type = float
            number = float(number)
        else:
            type = int
            number = int(number)
        return type, number

    def _define_math_sign(self) -> tuple:
        math_sign = ''
        while self._current_char and self._current_char in self._available_math_signs:
            math_sign += self._current_char
            self._forward()
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