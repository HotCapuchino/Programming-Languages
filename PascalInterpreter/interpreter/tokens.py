from enum import Enum, auto
import re


class TokenType(Enum):
    # num types
    INT = auto()
    FLOAT = auto()
    # operations
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    ASSIGN = auto()
    # other
    LPAREN = auto()
    RPAREN = auto()
    VAR = auto()
    EOS = auto()
    EOI = auto()
    EOP = auto()
    EOL = auto()
    SCOPE_START = auto()
    SCOPE_END = auto()

class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f'Token({self.type_}, {self.value})'

    def __repr__(self):
        return str(self)


FORBIDDEN_VARIABLE_NAMES = [
    'and',
    'array',
    'begin',
    'case',
    'const',
    'div',
    'do',
    'downto',
    'else',
    'end',
    'file',
    'for',
    'function',
    'goto',
    'if',
    'in',
    'label',
    'mod',
    'nil',
    'not',
    'of',
    'or',
    'packed',
    'procedure',
    'program',
    'record',
    'repeat',
    'set',
    'then',
    'to',
    'type',
    'until',
    'var',
    'while',
    'with'
]

AVAILABLE_VARIABLE_PATTERN = re.compile(r'[A-Za-z_]{1,}[A-Za-z_0-9]*')
AVAILABLE_VARIABLE_CHARS =  re.compile(r'[A-Za-z_0-9]')