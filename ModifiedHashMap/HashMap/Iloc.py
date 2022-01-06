from typing import Any

from .ModifiedDictErrors import InvalidDictIndexException

class Iloc():

    def __init__(self, linked_array: list) -> None:
        self.__linked_array = linked_array

    def __getitem__(self, __i: int) -> Any:
        if type(__i) is not int:
            raise InvalidDictIndexException('Wrong index type! Index should be of type int!')
        return self.__linked_array[__i][1]

    def __str__(self) -> str:
        return str(self.__linked_array)