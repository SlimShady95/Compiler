from Compiler.SyntaxKind import SyntaxKind

class SyntaxNode:
    def get_kind(self) -> SyntaxKind:
        raise NotImplementedError('Can not call abstract method.')

    def get_children(self):
        raise NotImplementedError('Can not call abstract method.')
