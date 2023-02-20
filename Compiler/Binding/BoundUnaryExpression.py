from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind
from Compiler.Binding.BoundUnaryOperator import BoundUnaryOperator


class BoundUnaryExpression(BoundExpression):
    """
        Contains a bound unary expression
    """

    # Bound unary operator
    _operator = None

    # Bound operand
    _operand = None

    def __init__(self, operator: BoundUnaryOperator, operand: BoundExpression) -> None:
        """
            Sets up all properties

            :param operator: BoundUnaryOperator
                The bound unary operator
            :param operand: BoundExpression
                The bound operand
            :return None
        """
        self._operator = operator
        self._operand = operand

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return BoundNodeKind.UNARY_EXPRESSION

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
        return [self._operator, self._operand]
