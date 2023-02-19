from Compiler.Binding.BoundBinaryOperator import BoundBinaryOperator
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundBinaryExpression(BoundExpression):
    _left = None
    _operator = None
    _right = None

    def __init__(self, left: BoundExpression, operator: BoundBinaryOperator, right: BoundExpression) -> None:
        self._left = left
        self._operator = operator
        self._right = right

    def get_kind(self) -> BoundNodeKind:
        return BoundNodeKind.BINARY_EXPRESSION

    def get_type(self) -> object:
        return self._left.get_type()

    def get_children(self) -> list:
        return [self._left, self._operator, self._right]