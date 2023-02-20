from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.SyntaxToken import SyntaxToken


class SyntaxTree:
    """
        Contains the syntax tree
    """

    # The root expression
    _root = None

    # The end of file token
    _end_of_file_token = None

    # A list containing all diagnostics
    _diagnostics = []

    def __init__(self, root: ExpressionSyntax, end_of_file_token: SyntaxToken, diagnostics: list) -> None:
        """
            Sets all all properties

            :param root: ExpressionSyntax
                The root expression of the syntax tree
            :param end_of_file_token: SyntaxToken
                The end of file token for the tree
            :param diagnostics: list
                A list containing all diagnostics from the steps before
            :return None
        """
        self._root = root
        self._end_of_file_token = end_of_file_token
        self._diagnostics = diagnostics

    def get_root(self) -> ExpressionSyntax:
        """
            Returns the root expression of the tree

            :return ExpressionSyntax
                Returns the root expression of the tree
        """
        return self._root
    
    def get_diagnostics(self) -> list:
        """
            Returns a list containing all diagnostics

            :return: list
                Returns a list containing all diagnostics
        """
        return self._diagnostics
