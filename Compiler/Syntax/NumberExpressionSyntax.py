from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxToken import SyntaxToken

class NumberExpressionSyntax(ExpressionSyntax):
    _token = None
    
    def __init__(self, token: SyntaxToken) -> None:
        self._token = token

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.NUMBER_EXPRESSION

    def get_children(self):
        return [self._token]
