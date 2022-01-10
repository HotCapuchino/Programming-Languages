from typing import Union
from interpreter.parser import Parser
from interpreter.tokens import TokenType
from .node import Empty, MultiOperation, Node, Number, BinaryOperation, UnaryOperation, Variable


class Interpreter:
    def __init__(self) -> None:
        self.variable_dict = {}
        self._parser = Parser()

    def __call__(self, text: str) -> Union[float, int]:
        if not text:
            return self.variable_dict

        syntax_tree = self._parser(text)
        if isinstance(syntax_tree, Empty):
            return self.variable_dict

        return self._visit(syntax_tree)

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

        return self.variable_dict

    def _visit_variable(self, node: Variable):
        if node.token.value not in self.variable_dict.keys():
            raise InterpreterException("Calling undefined variable!")
        return self.variable_dict[node.token.value]

    def _visit_number(self, node: Number) -> Union[float, int]:
        if node.token.type_ == TokenType.INT:
            return int(node.token.value)
        elif node.token.type_ == TokenType.FLOAT:
            return float(node.token.value)
            
    def _visit_binop(self, node: BinaryOperation) -> Union[float, int]:
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
            self.variable_dict[node.right.token.value] = self._visit(node.left)
            return
        raise InterpreterException("invalid operator")

    def _visit_unop(self, node: UnaryOperation) -> Union[float, int]:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left)
        if op.type_ == TokenType.MINUS:
            return 0 - self._visit(node.left)
        raise InterpreterException("invalid operator")

class InterpreterException(Exception):
    pass
