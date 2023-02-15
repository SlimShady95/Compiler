from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxNode import SyntaxNode


class ExpressionSyntax(SyntaxNode):
    def get_kind(self) -> SyntaxKind:
        pass

    def get_children(self) -> list:
        pass
