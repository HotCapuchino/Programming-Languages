from HashMap.ModifiedDictErrors import ParserException
from HashMap.Parser.lexer import Lexer
from HashMap.Parser.tokens import Token, TokenType


class Parser:
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise ParserException(f"Invalid expression - expected token type: {type_}")
        