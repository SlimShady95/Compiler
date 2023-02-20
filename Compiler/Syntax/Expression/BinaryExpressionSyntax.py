from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class BinaryExpressionSyntax(ExpressionSyntax):
    """
        Contains a binary expression syntax
    """

    # Left expression syntax
    _left = None

    # Operator token
    _operator = None

    # Right expression syntax
    _right = None
    
    def __init__(self, left: ExpressionSyntax, operator: SyntaxToken, right: ExpressionSyntax) -> None:
        """
            Sets up all properties

            :param left: ExpressionSyntax
                The left expression syntax
            :param operator: SyntaxToken
                The operator token
            :param right: ExpressionSyntax
                The right expression syntax
            :return None
        """
        self._left = left
        self._operator = operator
        self._right = right

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return SyntaxKind.BINARY_EXPRESSION

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._left, self._operator, self._right]
