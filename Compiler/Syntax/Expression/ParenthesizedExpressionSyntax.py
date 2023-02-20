from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class ParenthesizedExpressionSyntax(ExpressionSyntax):
    """
        Contains a parenthesized expression
    """

    # The opening parenthesis token
    _open_parenthesis_token = None

    # The expression inside
    _expression = None

    # The closing parenthesis token
    _close_parenthesis_token = None

    def __init__(self, open_token: SyntaxToken, expression: ExpressionSyntax, close_token: SyntaxToken) -> None:
        """
            Sets up all properties

            :param open_token: SyntaxToken
                The token of the opening parenthesis
            :param expression:
                The expression inside the parenthesis
            :param close_token:
                The token of the closing parenthesis
            :return None
        """
        self._open_parenthesis_token = open_token
        self._expression = expression
        self._close_parenthesis_token = close_token

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return SyntaxKind.PARENTHESIZED_EXPRESSION
    
    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._open_parenthesis_token, self._expression, self._close_parenthesis_token]
    
    def get_expression(self) -> ExpressionSyntax:
        """
            Returns the expression between the parenthesis

            :return ExpressionSyntax
                Returns the expression between the parenthesis
        """
        return self._expression
