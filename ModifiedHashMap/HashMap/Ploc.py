from .ModifiedDictErrors import InvalidDictIndexException, TokenException
from .Parser import Parser
from .Parser import Token, TokenCategory, TokenType, correct_condition_order, correct_key_order, tokens_to_exclude
import re

class Ploc():

    def __init__(self, linked_array: list) -> None:
        self._parser = Parser()
        self.__linked_array = linked_array
    
    def __getitem__(self, __k: str) -> dict:
        if type(__k) is not str:
            raise InvalidDictIndexException('Wrong index type! Index should be of type str!')
        mod_key = self.__prepare_key(__k)
        expression = self._parser.parse(mod_key)
        conditions = self._parser._exclude_tokens(self._parser.create_condtition(expression, correct_condition_order), tokens_to_exclude)
        return self.__filter_keys(conditions)
    
    def __prepare_key(self, key: str) -> str:
        return re.sub(r'[\(\)]', '', key).strip()

    def __filter_keys(self, conditions: list) -> dict:
        filtered_keys = {}
        for item in self.__linked_array:
            key = self.__prepare_key(item[0])
            expression = self._parser.parse(key)
            key_conditions = self._parser._exclude_tokens(self._parser.create_condtition(expression, correct_key_order), tokens_to_exclude)

            if len(conditions) == len(key_conditions):
                right_conditions_amount = 0

                for i in range(len(conditions)):
                    condition_math_sign = list(filter(lambda item: item.category == TokenCategory.CONDITION, conditions[i]))[0]
                    condition_value = list(filter(lambda item: item.category == TokenCategory.DIGIT, conditions[i]))[0]
                    key_value = list(filter(lambda item: item.category == TokenCategory.DIGIT, key_conditions[i]))[0]

                    if self.__check_condtition(condition_value, condition_math_sign, key_value):
                        right_conditions_amount += 1
                    
                if right_conditions_amount == len(key_conditions):
                    filtered_keys[item[0]] = item[1]
                    
        return filtered_keys 

    def __check_condtition(self, condition_value: Token, condition_sign: Token, key_value: Token) -> bool:
        if condition_sign.type_ == TokenType.EQUAL:
            return condition_value.value == key_value.value
        elif condition_sign.type_ == TokenType.GREATER:
            return key_value.value > condition_value.value
        elif condition_sign.type_ == TokenType.GREATER_OR_EQUAL:
            return key_value.value >= condition_value.value
        elif condition_sign.type_ == TokenType.LESS:
            return key_value.value < condition_value.value
        elif condition_sign.type_ == TokenType.LESS_OR_EQUAL:
            return key_value.value <= condition_value.value
        elif condition_sign.type_ == TokenType.NOT_EQUAL:
            return condition_value.value != key_value.value
        raise TokenException('Unknown token type for math condition!')

    def __str__(self) -> str:
        return str(self.__linked_array)