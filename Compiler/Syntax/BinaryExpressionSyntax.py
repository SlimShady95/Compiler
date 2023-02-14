from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxToken import SyntaxToken

class BinaryExpressionSyntax(ExpressionSyntax):
    _left = None
    _operator = None
    _right = None
    
    def __init__(self, left: ExpressionSyntax, operator: SyntaxKind, right: ExpressionSyntax) -> None:
        self._left = left
        self._operator = operator
        self._right = right

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.BINARY_EXPRESSION

    def get_children(self):
        return [self._left, self._operator, self._right]
