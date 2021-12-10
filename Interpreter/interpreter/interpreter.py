from interpreter.tokens import TokenType
from .node import Node, Number, BinaryOperation, UnaryOperation


class Interpreter:
    def __call__(self, tree: Node) -> float:
        return self._visit(tree)

    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, UnaryOperation):
            return self._visit_unop(node)
        elif isinstance(node, BinaryOperation):
            return self._visit_binop(node)
        else:
            raise InterpreterException("invalid node")

    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)

    def _visit_binop(self, node: BinaryOperation) -> float:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left) + self._visit(node.right)
        if op.type_ == TokenType.MINUS:
            return self._visit(node.left) - self._visit(node.right)
        if op.type_ == TokenType.MUL:
            return self._visit(node.left) * self._visit(node.right)
        if op.type_ == TokenType.DIV:
            return self._visit(node.left) / self._visit(node.right)
        raise InterpreterException("invalid operator")

    def _visit_unop(self, node: UnaryOperation) -> float:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left)
        if op.type_ == TokenType.MINUS:
            return 0 - self._visit(node.left)
        raise InterpreterException("invalid operator")


class InterpreterException(Exception):
    pass
