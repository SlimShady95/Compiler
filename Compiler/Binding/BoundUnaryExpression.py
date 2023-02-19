from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind
from Compiler.Binding.BoundUnaryOperator import BoundUnaryOperator


class BoundUnaryExpression(BoundExpression):
    _operator = None
    _operand = None

    def __init__(self, operator: BoundUnaryOperator, operand: BoundExpression) -> None:
        self._operator = operator
        self._operand = operand

    def get_kind(self) -> BoundNodeKind:
        return BoundNodeKind.UNARY_EXPRESSION

    def get_type(self) -> object:
        return self._operator.get_type()

    def get_children(self) -> list:
        return [self._operator, self._operand]
