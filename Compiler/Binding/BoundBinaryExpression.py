from Compiler.Binding.BoundBinaryOperator import BoundBinaryOperator
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundBinaryExpression(BoundExpression):
    """
        Contains a bound binary expression
    """

    # Left bound expression
    _left = None

    # Bound binary operator
    _operator = None

    # Right bound expression
    _right = None

    def __init__(self, left: BoundExpression, operator: BoundBinaryOperator, right: BoundExpression) -> None:
        """
            Sets up all properties

            :param left: BoundExpression
                The left bound expression
            :param operator: BoundBinaryOperator
                The bound binary operator
            :param right: BoundExpression
                The right bound expression
            :return None
        """
        self._left = left
        self._operator = operator
        self._right = right

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return BoundNodeKind.BINARY_EXPRESSION

    def get_type(self) -> object:
        """
            Returns the type of the operator

            :return object
                Returns the type of the operator
        """
        return self._operator.get_type()

    def get_children(self) -> list:
        """
            Returns a list containing all children of this node

            :return list
                Returns a list containing all children of this node
        """
        return [self._left, self._operator, self._right]
