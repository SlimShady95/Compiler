from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundVariableExpression(BoundExpression):
    """
        Contains a bound binary expression
    """

    # The name of the variable
    _name = None

    # The type of the variable
    _type = None

    def __init__(self, name: str, type_: object) -> None:
        """
            Sets up all properties

            :param name: str
                The name of the variable
            :param type_: object
                The type of the variable
            :return None
        """
        self._name = name
        self._type = type_

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
        return self._type

    def get_name(self) -> str:
        """
            Returns the name of the variable

            :return str
                Returns the name of the variable
        """
        return self._name
