from HashMap.ModifiedDictErrors import ParserException
from .lexer import Lexer
from .tokens import Token, TokenType
from copy import deepcopy


class Parser:
    
    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def parse(self, text: str) -> list:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._get_expression()

    def _get_expression(self) -> None:
        expression = []
        while self._current_token.type_ != TokenType.EOS:
            expression.append(self._current_token)
            self._current_token = self._lexer.next()
        return expression

    def create_condtition(self, token_list: list, correct_token_order: list) -> list:
        current_order = []
        conditions = []

        for token in token_list:

            if not len(current_order) or len(current_order) == len(correct_token_order):

                if token.category != correct_token_order[0]:
                    raise ParserException('Invalid condition!')

                if len(current_order) == len(correct_token_order):
                    conditions.append(deepcopy(current_order))

                current_order.clear()
                current_order.append(token)
            else:
                current_order.append(token)

                if not self._check_token_order(current_order, correct_token_order):
                    raise ParserException('Invalid condition!')

        # проверка последнего условия, которое может быть без разделителя в конце, (т.е. без ,)
        if len(current_order) == len(correct_token_order) - 1:
            if not self._check_token_order(current_order, correct_token_order):
                 raise ParserException('Invalid condition!')
            
            conditions.append(deepcopy(current_order))
                
        return conditions 
        
    def _check_token_order(self, current_order: list, correct_order: list) -> bool:
        current_categories_order = list(map(lambda item: item.category, current_order))
        if current_categories_order != correct_order[:len(current_order)]:
            return False
        return True

    def _exclude_tokens(self, conditions: list, tokens_to_exclude: list) -> list:
        new_conditions = []
        for condition in conditions:
            new_condition = []
            for token in condition:
                if not token.category in tokens_to_exclude:
                    new_condition.append(token)
            new_conditions.append(new_condition)
        return new_conditions