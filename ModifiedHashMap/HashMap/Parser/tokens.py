from enum import Enum, auto

class TokenType(Enum):
    FLOAT: auto()
    INTEGER: auto()
    GREATER: auto()
    LESS: auto()
    EQUAL: auto()
    NOT_EQUAL: auto()
    GREATER_OR_EQUAL: auto()
    LESS_OR_EQUAL: auto()
    COMMA: auto()
    EOS: auto()

class AVAILABLE_MATH_SIGNS(Enum):
    LESS = '<'
    GREATER = '>'
    EQUAL = '='

class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f'Token({self.type_}, {self.value})'

    def __repr__(self):
        return str(self)