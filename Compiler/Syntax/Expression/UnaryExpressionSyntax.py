from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class UnaryExpressionSyntax(ExpressionSyntax):
    """
        Contains a unary expression syntax
    """

    # The operator of the expression
    _operator = None

    # The operand of the expression
    _operand = None

    def __init__(self, operator: SyntaxToken, operand: ExpressionSyntax) -> None:
        """
            Sets up all properties

            :param operator: SyntaxToken
                The syntax token of the operator
            :param operand: ExpressionSyntax
                The expression syntax used as operand
        """
        self._operator = operator
        self._operand = operand

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of this expression

            :return BoundNodeKind
                Returns the kind of this expression
        """
        return SyntaxKind.UNARY_EXPRESSION

    def get_children(self) -> list:
        """
             Returns a list containing all children of this expression

             :return list
                 Returns a list containing all children of this expression
         """
        return [self._operator, self._operand]
