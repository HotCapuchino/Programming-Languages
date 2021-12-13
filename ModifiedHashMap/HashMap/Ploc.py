from typing import Any
from HashMap.Iloc import Iloc
from HashMap.ModifiedDictErrors import InvalidDictIndexException
from HashMap.Parser.parser import Parser

class Ploc(Iloc):

    def __init__(self, linked_array: list) -> None:
        self.parser = Parser()
        super().__init__(linked_array)
    
    def __getitem__(self, __k: str) -> Any:
        if type(__k) is not str:
            raise InvalidDictIndexException('Wrong index type! Index should be of type str!')
        
        