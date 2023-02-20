from Compiler.Binding.BoundNode import BoundNode
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundExpression(BoundNode):
    """
        Base class for bound expressions
    """

    def get_kind(self) -> BoundNodeKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        raise NotImplementedError('Can not call abstract method.')

    def get_type(self) -> object:
        """
            Returns the type of the operator

            :return object
                Returns the type of the operator
        """
        raise NotImplementedError('Can not call abstract method.')

    def get_children(self) -> list:
        """
            Returns a list containing all children of this node

            :return list
                Returns a list containing all children of this node
        """
        return []
