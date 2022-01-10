import pytest
from interpreter import Lexer, LexerException
from interpreter.tokens import TokenType

@pytest.fixture
def testLexer() -> Lexer:
    return Lexer()

class TestLexer:

    def test_creation(self, testLexer: Lexer):
        testLexer.init('')
        assert testLexer._text == '' and testLexer._pos == 0

    def test_EOL(self, testLexer: Lexer):
        testLexer.init(' \t\n')
        token = testLexer.next()
        assert token.type_ == TokenType.EOL

    def test_EOI(self, testLexer: Lexer):
        testLexer.init(';')
        token = testLexer.next()
        assert token.type_ == TokenType.EOI

    def test_EOP(self, testLexer: Lexer):
        testLexer.init('.')
        token = testLexer.next()
        assert token.type_ == TokenType.EOP

    def test_PLUS(self, testLexer: Lexer):
        testLexer.init('+')
        token = testLexer.next()
        assert token.type_ == TokenType.PLUS

    def test_MINUS(self, testLexer: Lexer):
        testLexer.init('-')
        token = testLexer.next()
        assert token.type_ == TokenType.MINUS

    def test_MUL(self, testLexer: Lexer):
        testLexer.init('*')
        token = testLexer.next()
        assert token.type_ == TokenType.MUL

    def test_DIV(self, testLexer: Lexer):
        testLexer.init('/')
        token = testLexer.next()
        assert token.type_ == TokenType.DIV

    def test_LPAREN(self, testLexer: Lexer):
        testLexer.init('(')
        token = testLexer.next()
        assert token.type_ == TokenType.LPAREN

    def test_RPAREN(self, testLexer: Lexer):
        testLexer.init(')')
        token = testLexer.next()
        assert token.type_ == TokenType.RPAREN
    
    def test_EOS(self, testLexer: Lexer):
        testLexer.init('')
        token = testLexer.next()
        assert token.type_ == TokenType.EOS

    def test_wrong_token(self, testLexer: Lexer):
        testLexer.init('?')
        with pytest.raises(LexerException):
            testLexer.next()

    def test_assignment(self, testLexer: Lexer):
        testLexer.init(':=')
        token = testLexer.next()
        assert token.type_ == TokenType.ASSIGN

    def test_wrong_assignment(self, testLexer: Lexer):
        testLexer.init(':==')
        with pytest.raises(LexerException):
            testLexer.next()
    
    def test_int(self, testLexer: Lexer):
        testLexer.init('4')
        token = testLexer.next()
        assert token.type_ == TokenType.INT and token.value == 4

    def test_float(self, testLexer: Lexer):
        testLexer.init('4.0')
        token = testLexer.next()
        assert token.type_ == TokenType.FLOAT and token.value == 4.0

    def test_wrong_num1(self, testLexer: Lexer):
        testLexer.init('4.0.0')
        with pytest.raises(LexerException):
            testLexer.next()

    def test_wrong_num2(self, testLexer: Lexer):
        testLexer.init('4.')
        with pytest.raises(LexerException):
            testLexer.next()

    def test_var_name(self, testLexer: Lexer):
        testLexer.init('y ')
        token = testLexer.next()
        assert token.type_ == TokenType.VAR and token.value == 'y'

    def test_forbidden_var_name(self, testLexer: Lexer):
        testLexer.init('for ')
        with pytest.raises(LexerException):
            testLexer.next()

    def test_scope_start(self, testLexer: Lexer):
        testLexer.init('BEGIN ')
        token = testLexer.next()
        assert token.type_ == TokenType.SCOPE_START and token.value == 'BEGIN'

    def test_scope_end(self, testLexer: Lexer):
        testLexer.init('END ')
        token = testLexer.next()
        assert token.type_ == TokenType.SCOPE_END and token.value == 'END'