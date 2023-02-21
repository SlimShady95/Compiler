from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class NameExpressionSyntax(ExpressionSyntax):
    """
        Contains a named expression syntax
    """

    # The identifier token of the expression
    _identifier_token = None

    def __init__(self, identifier_token: SyntaxToken) -> None:
        """
            Sets up all properties

            :param identifier_token: SyntaxToken
                The identifier token of this name expression
            :return None
        """
        self._identifier_token = identifier_token

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return SyntaxKind.NAME_EXPRESSION

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._identifier_token]
