from interpreter.lexer import Lexer
from interpreter.node import BinaryOperation, MultiOperation, Node, Number, UnaryOperation, Variable
from interpreter.tokens import Token, TokenType


class Parser:
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def parse(self, text: str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._program()

    def __call__(self, text: str) -> Node:
        return self.parse(text)

    def _program(self) -> Node:
        result = self._complex_statement()
        self._check_token_type(TokenType.EOP)
        return result
    
    def _complex_statement(self, wrapped = False) -> Node:
        token = self._current_token
        result = None
        if token.type_ == TokenType.SCOPE_START:
            self._check_token_type(TokenType.SCOPE_START)
            self._check_token_type(TokenType.EOL)
            result = self._statement_list()
            self._check_token_type(TokenType.SCOPE_END)
        return result

    def _statement_list(self) -> Node:
        token = self._current_token
        if token.type_ == TokenType.SCOPE_END:
            return None

        statements = []
        first = self._statement()
        statements.append(first)

        while self._current_token.type_ != TokenType.SCOPE_END:
            statement = self._statement()
            statements.append(statement)

        return MultiOperation(statements)
        

    def _statement(self) -> Node:
        token = self._current_token
        if token.type_ == TokenType.SCOPE_START:
            result = self._complex_statement()
            self._check_token_type(TokenType.EOI, True)
            self._check_token_type(TokenType.EOL)
        else:
            result = self._assignment()
            # it's available in pascal to skip semicolon after instruction, if it's followed by END operator
            # TODO Check token type 
            current_token = self._current_token 
            self._current_token = self._lexer.next()
            token_to_check = self._current_token

            if token_to_check.type_ != TokenType.SCOPE_END:
                if current_token.type_ != TokenType.EOI:
                    raise ParserException(f"Invalid expression - expected token type: {TokenType.EOI}")
                self._check_token_type(TokenType.EOL)

        return result

    def _assignment(self) -> Node:
        var = self._variable()
        token = self._current_token
        self._check_token_type(TokenType.ASSIGN)
        var_value = self._expr()    
        return BinaryOperation(var_value, token, var)

    def _variable(self) -> Node:
        token = self._current_token
        self._check_token_type(TokenType.VAR)
        return Variable(token)

    def _expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()

        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)              
            result = BinaryOperation(result, token, self._term())
        return result

    def _term(self) -> Node:
        result = self._factor()
        ops = [TokenType.MUL, TokenType.DIV]

        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinaryOperation(result, token, self._factor())
        return result

    def _factor(self) -> Node:
        token = self._current_token
        
        if token.type_ == TokenType.FLOAT:
            self._check_token_type(TokenType.FLOAT)
            return Number(token, TokenType.FLOAT)
        elif token.type_ == TokenType.INT:
            self._check_token_type(TokenType.INT)
            return Number(token, TokenType.INT)
        elif token.type_ == TokenType.VAR:
            self._check_token_type(TokenType.VAR)
            return Variable(token)
        elif token.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)
            return UnaryOperation(token, self._factor())
        elif token.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
            return UnaryOperation(token, self._factor())
        elif token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        else:
            raise ParserException(f"Invalid factor - {token.type_}")

    def _check_token_type(self, type_: TokenType, gentle=False):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            if not gentle:
                raise ParserException(f"Invalid expression - expected token type: {type_}")

class ParserException(Exception):
    pass
