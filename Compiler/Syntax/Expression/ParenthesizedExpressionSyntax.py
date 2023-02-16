from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken


class ParenthesizedExpressionSyntax(ExpressionSyntax):
    _open_parenthesis_token = None
    _expression = None
    _close_parenthesis_token = None

    def __init__(self, open_token: SyntaxToken, expression: ExpressionSyntax, close_token: SyntaxToken) -> None:
        self._open_parenthesis_token = open_token
        self._expression = expression
        self._close_parenthesis_token = close_token

    def get_kind(self) -> SyntaxKind:
        return SyntaxKind.PARENTHESIZED_EXPRESSION
    
    def get_children(self) -> list:
        return [self._open_parenthesis_token, self._expression, self._close_parenthesis_token]
    
    def get_expression(self) -> ExpressionSyntax:
        return self._expression
