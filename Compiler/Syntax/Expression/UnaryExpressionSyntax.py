from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class UnaryExpressionSyntax(ExpressionSyntax):
    _operator = None
    _operand = None

    def __init__(self, operator: SyntaxToken, operand: ExpressionSyntax) -> None:
        self._operator = operator
        self._operand = operand

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.UNARY_EXPRESSION

    def get_children(self) -> list:
        return [self._operator, self._operand]
