from typing import Any
from HashMap.ModifiedDictErrors import InvalidDictIndexException
from HashMap.Parser.parser import Parser
from HashMap.Parser.tokens import Token, TokenCategory, TokenType, correct_condition_order, correct_key_order, tokens_to_exclude
import re

class Ploc():

    def __init__(self, linked_array: list) -> None:
        self._parser = Parser()
        self.__linked_array = linked_array
    
    def __getitem__(self, __k: str) -> Any:
        if type(__k) is not str:
            raise InvalidDictIndexException('Wrong index type! Index should be of type str!')
        mod_key = self.__prepare_key(__k)
        expression = self._parser.parse(mod_key)
        conditions = self._parser._exclude_tokens(self._parser.create_condtition(expression, correct_condition_order), tokens_to_exclude)
        print(conditions)
        # return self.__filter_keys(conditions)
    
    def __prepare_key(self, key: str) -> str:
        return re.sub(r'[\(\)]', '', key).strip()

    def __filter_keys(self, conditions: list) -> None:
        filtered_keys = []
        for item in self.__linked_array:
            key = item[0]
            expression = self._parser.parse(key)
            key_conditions = self._parser(self._parser.create_condtition(expression, correct_key_order), tokens_to_exclude)

            if len(conditions) == len(key_conditions):
                right_conditions_amount = 0

                for i in range(len(conditions)):
                    pass
                    # condition_math_signs = list(filter(lambda item: item.category == TokenCategory.CONDITION, conditions[i]))
                    # condition_values = list(filter(lambda item: item.category == TokenCategory.DIGIT, conditions[i]))
                    # condition_items = zip(condition_values, condition_math_signs)
                    # key_values = list(filter(lambda item: item.category == TokenCategory.DIGIT, key_conditions[i]))
                    # if len(key_values) != len(condition_items):
                    #     # TODO throw Exception
                    #     pass
                    # for j in range(len(condition_items)):
                    #     if self.__check_condtition(condition_items[j][0], condition_items[j][1], key_values[j]):
                    #         right_conditions_amount += 1
                    
                if right_conditions_amount == len(key_conditions):
                    filtered_keys.append(item[1])
                    
        return filtered_keys 

    def __check_condtition(self, condition_value: Token, condition_sign: Token, key_value: Token) -> bool:
        if condition_sign.type_ == TokenType.EQUAL:
            return condition_value.value == key_value.value
        elif condition_sign.type_ == TokenType.GREATER:
            return condition_value > key_value.value
        elif condition_sign.type_ == TokenType.GREATER_OR_EQUAL:
            return condition_value >= key_value.value
        elif condition_sign.type_ == TokenType.LESS:
            return condition_value < key_value.value
        elif condition_sign.type_ == TokenType.LESS_OR_EQUAL:
            return condition_value <= key_value.value
        elif condition_sign.type_ == TokenType.NOT_EQUAL:
            return condition_value != key_value.value
        # TODO throw Exception
