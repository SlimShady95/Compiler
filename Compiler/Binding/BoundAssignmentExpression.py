from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind
from Compiler.Type.VariableSymbol import VariableSymbol


class BoundAssignmentExpression(BoundExpression):
    """
        Contains a bound assignment expression
    """

    # The instance of the variable symbol
    _variable = None

    # The expression of the assignment
    _expression = None

    def __init__(self, variable: VariableSymbol, expression: BoundExpression) -> None:
        """
            Sets up all properties

            :param variable: VariableSymbol
                The instance of the variable symbol
            :param expression: BoundExpression
                The expression of the assignment
            :return None
        """
        self._variable = variable
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
