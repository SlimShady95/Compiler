from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxToken import SyntaxToken


class SyntaxTree:
    _root = None
    _end_of_file_token = None
    _diagnostics = []

    def __init__(self, root: ExpressionSyntax, end_of_file_token: SyntaxToken, diagnostics: list) -> None:
        self._root = root
        self._end_of_file_token = end_of_file_token
        self._diagnostics = diagnostics

    def get_root(self) -> ExpressionSyntax:
        return self._root
    
    def get_diagnostics(self) -> list:
        return self._diagnostics
