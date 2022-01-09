from typing import Union
from interpreter.tokens import TokenType
from .node import MultiOperation, Node, Number, BinaryOperation, UnaryOperation, Variable


class Interpreter:
    def __init__(self) -> None:
        self.vaiable_dict = {}

    def __call__(self, tree: Node) -> Union[float, int]:
        return self._visit(tree)

    def _visit(self, node: Node) -> Union[float, int]:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, UnaryOperation):
            return self._visit_unop(node)
        elif isinstance(node, BinaryOperation):
            return self._visit_binop(node)
        elif isinstance(node, MultiOperation):
            return self._visit_multiop(node)
        elif isinstance(node, Variable):
            return self._visit_variable(node)
        else:
            raise InterpreterException("Invalid node")

    def _visit_multiop(self, node: MultiOperation):
        for statement in node.nodes:
            self._visit(statement)

        return self.vaiable_dict

    def _visit_variable(self, node: Variable):
        if node.token.value not in self.vaiable_dict.keys():
            raise InterpreterException("Calling undefined variable!")
        return self.vaiable_dict[node.token.value]

    def _visit_number(self, node: Number) -> Union[float, int]:
        if node.token.type_ == TokenType.INT:
            return int(node.token.value)
        elif node.token.type_ == TokenType.FLOAT:
            return float(node.token.value)
            
    def _visit_binop(self, node: BinaryOperation) -> Union[float, int]:
        if not self._check_binop_types(node.left, node.right):
            raise IncompatibleTypesException(f'Incompatible types with {type(node.left)} and {type(node.right)}!')

        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left) + self._visit(node.right)
        if op.type_ == TokenType.MINUS:
            return self._visit(node.left) - self._visit(node.right)
        if op.type_ == TokenType.MUL:
            return self._visit(node.left) * self._visit(node.right)
        if op.type_ == TokenType.DIV:
            return self._visit(node.left) / self._visit(node.right)
        if op.type_ == TokenType.ASSIGN:
            self.vaiable_dict[node.right.token.value] = self._visit(node.left)
            return
        raise InterpreterException("invalid operator")

    def _visit_unop(self, node: UnaryOperation) -> Union[float, int]:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left)
        if op.type_ == TokenType.MINUS:
            return 0 - self._visit(node.left)
        raise InterpreterException("invalid operator")

    def _check_binop_types(self, left, right) -> bool:
        if isinstance(left, Number) and isinstance(right, Number):
            if type(left) != type(right):
                return False
        return True

class InterpreterException(Exception):
    pass

class IncompatibleTypesException(Exception):
    pass
