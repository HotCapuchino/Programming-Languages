from enum import Enum, auto

class TokenType(Enum):
    FLOAT = auto()
    INTEGER = auto()
    GREATER = auto()
    LESS = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_OR_EQUAL = auto()
    LESS_OR_EQUAL = auto()
    COMMA = auto()
    EOS = auto()

class TokenCategory(Enum):
    DIGIT = auto()
    DIVIDER = auto()
    CONDITION = auto()
    NONE = auto()

class MATH_SIGNS(Enum):
    LESS = '<'
    GREATER = '>'
    EQUAL = '='

class Token:

    def __init__(self, type_: TokenType, value: str, category: TokenCategory = TokenCategory.NONE) -> None:
        self.type_ = type_
        self.value = value
        self.category = category

    # For debugging
    # def __str__(self) -> str:
    #     return f'Token({self.type_}, {self.value}, {self.category})'

    # def __repr__(self) -> str:
    #     return str(self)

correct_condition_order = [TokenCategory.CONDITION, TokenCategory.DIGIT, TokenCategory.DIVIDER]
correct_key_order = [TokenCategory.DIGIT, TokenCategory.DIVIDER]
tokens_to_exclude = [TokenCategory.DIVIDER]