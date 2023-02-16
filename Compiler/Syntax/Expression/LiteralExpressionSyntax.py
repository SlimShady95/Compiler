from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class LiteralExpressionSyntax(ExpressionSyntax):
    _token = None
    
    def __init__(self, token: SyntaxToken) -> None:
        self._token = token

    def get_token(self) -> SyntaxToken:
        return self._token

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.LITERAL_EXPRESSION

    def get_children(self) -> list:
        return [self._token]
