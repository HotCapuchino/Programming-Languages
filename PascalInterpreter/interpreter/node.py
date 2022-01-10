from interpreter.tokens import Token


class Node():
    pass
    # for debugging only
    # def __str__(self) -> str:
    #     return f"{self.__class__.__name__}"

class Empty(Node):
    pass
    # for debugging only
    # def __str__(self) -> str:
    #     return f"EMPTY NODE"

class Number(Node):

    def __init__(self, token: Token, type_) -> None:
        self.token = token
        self.type_ = type_
        super().__init__()

    # for debugging only
    # def __str__(self) -> str:
    #     return f"Number({self.token})"

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, Number):
           return node.token == self.token and node.type_ == self.type_
        return False


class Variable(Node):
    
    def __init__(self, token: Token) -> None:
        self.token = token
        super().__init__()

    # for debugging only
    # def __str__(self) -> str:
    #     return f"Variable({self.token})"

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, Variable):
            return node.token == self.token
        return False


class BinaryOperation(Node): # Statement, Assignment, Program

    def __init__(self, left: Node, operation: Token, right: Node) -> None:
        self.left = left
        self.operation = operation
        self.right = right

    # for debugging only
    # def __str__(self) -> str:
    #     return f"BinaryOperation: {self.operation.value} (left: {self.left}, right: {self.right})"

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, BinaryOperation):
            return node.operation == self.operation and node.left == self.left and node.right == self.right
        return False


class UnaryOperation(Node):
    
    def  __init__(self, operation: Token, left: Node) -> None:
        self.operation = operation
        self.left = left

    # for debugging only
    # def __str__(self) -> str:
    #     return f"UnaryOperation: {self.operation.value} node: {self.left}"

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, UnaryOperation):
            return node.operation == self.operation and node.left == self.left
        return False

class MultiOperation(Node): # Complex Statement
    
    def __init__(self, nodes: list) -> None:
        self.nodes = nodes

    # for debugging only
    # def __str__(self) -> str:
    #     res_str = 'MultiOperation: '
    #     for node in self.nodes:
    #         res_str += str(node)
    #     return res_str

    def __eq__(self, node: Node) -> bool:
        if isinstance(node, MultiOperation):
            return node.nodes == self.nodes
        return False
