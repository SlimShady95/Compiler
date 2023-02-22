from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind
from Compiler.Type.VariableSymbol import VariableSymbol


class BoundVariableExpression(BoundExpression):
    """
        Contains a bound variable expression
    """

    # The instance of the variable symbol
    _variable = None

    def __init__(self, variable: VariableSymbol) -> None:
        """
            Sets up all properties

            :param variable: VariableSymbol
                The instance of the variable symbol
            :return None
        """
        self._variable = variable

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return BoundNodeKind.VARIABLE_EXPRESSION

    def get_type(self) -> object:
        """
            Returns the type of the variable

            :return object
                Returns the type of the variable
        """
        return self._variable.get_type()

    def get_name(self) -> str:
        """
            Returns the name of the variable

            :return str
                Returns the name of the variable
        """
        return self._variable.get_name()

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._variable]
