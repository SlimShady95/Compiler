from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxNode import SyntaxNode


class ExpressionSyntax(SyntaxNode):
    """
        Base class for expression syntax
    """

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        raise NotImplementedError('Can not call abstract method.')

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        raise NotImplementedError('Can not call abstract method.')
