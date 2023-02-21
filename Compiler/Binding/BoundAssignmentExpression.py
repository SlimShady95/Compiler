from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundAssignmentExpression(BoundExpression):
    """
        Contains a bound binary expression
    """

    # The name of the variable
    _name = None

    # The expression of the assignment
    _expression = None

    def __init__(self, name: str, expression: BoundExpression) -> None:
        """
            Sets up all properties

            :param name: str
                The name of the variable
            :param expression: BoundExpression
                The expression of the assignment
            :return None
        """
        self._name = name
        self._expression = expression

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return BoundNodeKind.ASSIGNMENT_EXPRESSION

    def get_type(self) -> object:
        """
            Returns the type of the expression

            :return object
                Returns the type of the expression
        """
        return self._expression.get_type()

    def get_name(self) -> str:
        """
            Returns the name of the variable

            :return str
                Returns the name of the variable
        """
        return self._name

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._expression]
