from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundLiteralExpression(BoundExpression):
    """
        Contains a bound literal expression
    """

    # The value of the expression
    _value = None

    def __init__(self, value) -> None:
        """
            Sets up the value

            :param value
                The value of the expression
        """
        self._value = value

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        raise BoundNodeKind.LITERAL_EXPRESSION

    def get_type(self) -> object:
        """
            Returns the type of the operator

            :return object
                Returns the type of the operator
        """
        return type(self._value)

    def get_value(self):
        """
            Returns the value of the expression

            :return mixed
                Returns the value of the expression
        """
        return self._value
