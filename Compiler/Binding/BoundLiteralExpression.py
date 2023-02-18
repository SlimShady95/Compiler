from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundLiteralExpression(BoundExpression):
    _value = None

    def __init__(self, value) -> None:
        self._value = value

    def get_kind(self) -> BoundNodeKind:
        raise BoundNodeKind.LITERAL_EXPRESSION

    def get_type(self) -> object:
        return type(self._value)

    def get_value(self):
        return self._value