from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class LiteralExpressionSyntax(ExpressionSyntax):
    _token = None
    _value = None
    
    def __init__(self, token: SyntaxToken, value: object = None) -> None:
        self._token = token
        self._value = value if value is not None else token.get_value()

    def get_token(self) -> SyntaxToken:
        return self._token

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.LITERAL_EXPRESSION

    def get_children(self) -> list:
        return [self._token]

    def get_value(self) -> object:
        return self._value
