from typing import Any

class Iloc(list):

    def __init__(self, linked_array: list) -> None:
        self.__linked_array = linked_array
        # print(self.__linked_array)

    def __add__(self, __x: list) -> None:
        return None

    def append(self, __object) -> None:
        return None

    def __delitem__(self, __i) -> None:
        return None

    def __getitem__(self, __i) -> Any:
        return self.__linked_array[__i][1]

    def pop(self, __index) -> None:
        return None

    def clear(self) -> None:
        return None

    def insert(self, __index, __object) -> None:
        return None

    def remove(self, __value) -> None:
        return None