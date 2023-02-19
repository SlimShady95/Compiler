from Compiler.Syntax.SyntaxKind import SyntaxKind


class SyntaxNode:
    """
        Base class for syntax nodes
    """
    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of the syntax node

            :return SyntaxKind
                Returns the kind of the syntax node
        """
        raise NotImplementedError('Can not call abstract method.')

    def get_children(self) -> list:
        """
            Returns a list with all children of the node

            :return list
                Returns a list with all children of the node
        """
        raise NotImplementedError('Can not call abstract method.')
