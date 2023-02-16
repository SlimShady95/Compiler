from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxNode import SyntaxNode


class ExpressionSyntax(SyntaxNode):
    def get_kind(self) -> SyntaxKind:
        pass

    def get_children(self) -> list:
        pass
