from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class LiteralExpressionSyntax(ExpressionSyntax):
    """
        Contains a literal expression syntax
    """

    # The syntax token of the expression
    _token = None

    # The value of the expression
    _value = None
    
    def __init__(self, token: SyntaxToken, value: object = None) -> None:
        """
            Sets up all properties

            :param token: SyntaxToken
                The syntax token of the expression
            :param value: object
                The value of the expression
            :return None
        """
        self._token = token
        self._value = value if value is not None else token.get_value()

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return SyntaxKind.LITERAL_EXPRESSION

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._token]

    def get_token(self) -> SyntaxToken:
        """
            Returns the token of the expression

            :return SyntaxToken
                Returns the token of the expression
        """
        return self._token

    def get_value(self) -> object:
        """
            Returns the value of the expression

            :return object
                Returns the value of the object
        """
        return self._value
