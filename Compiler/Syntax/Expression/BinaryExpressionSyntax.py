from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class BinaryExpressionSyntax(ExpressionSyntax):
    _left = None
    _operator = None
    _right = None
    
    def __init__(self, left: ExpressionSyntax, operator: SyntaxToken, right: ExpressionSyntax) -> None:
        self._left = left
        self._operator = operator
        self._right = right

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.BINARY_EXPRESSION

    def get_children(self) -> list:
        return [self._left, self._operator, self._right]