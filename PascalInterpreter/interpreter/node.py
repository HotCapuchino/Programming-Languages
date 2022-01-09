
from typing import Union
from interpreter.tokens import Token


class Node():
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class Number(Node):

    def __init__(self, token: Token, type_) -> None:
        self.token = token
        self.type_ = type_
        super().__init__()

    def __str__(self) -> str:
        return f"Number({self.token})"


class Variable(Node):
    
    def __init__(self, token: Token) -> None:
        self.token = token
        super().__init__()

    def __str__(self) -> str:
        return f"Variable({self.token})"


class BinaryOperation(Node): # Statement, Assignment, Program

    def __init__(self, left: Node, operation: Token, right: Node) -> None:
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self) -> str:
        return f"BinaryOperation: {self.operation.value} (left: {self.left}, right: {self.right})"


class UnaryOperation(Node):
    
    def  __init__(self, operation: Token, left: Node) -> None:
        self.operation = operation
        self.left = left

    def __str__(self) -> str:
        return f"UnaryOperation: {self.operation.value} node: {self.left}"


class MultiOperation(Node): # Complex Statement
    
    def __init__(self, nodes: list) -> None:
        self.nodes = nodes

    def __str__(self) -> str:
        res_str = ''
        for node in self.nodes:
            res_str += str(node)
        return res_str
