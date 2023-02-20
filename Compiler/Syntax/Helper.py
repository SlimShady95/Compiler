from Compiler.Compilation import Compilation
from Compiler.Syntax.SyntaxNode import SyntaxNode
from Compiler.Syntax.Parser import Parser


def pretty_print(node: SyntaxNode, indent='', is_last=True) -> None:
    """
        Pretty prints the given node and its children to represent the syntax tree

        :param node: SyntaxNode
            The root node to print
        :param indent: string
            The indent for the current depth
        :param is_last: bool
            If set to true, there will be the closing marker (└──) for the tree,
            otherwise it will be the normal marker (├──)
        :return None        
    """
    marker = '└──' if is_last else '├──'
    print(indent, marker, node.get_kind(), sep='')

    indent += '    ' if is_last else '│   '
    children = node.get_children()
    for child in children:
        pretty_print(child, indent, child == children[-1])


def evaluate(source: str) -> dict:
    """
        Takes the given source code and evaluates it

        :param source: string
            The source code which should be executed
        :return dict
            Returns a dictionary containing the result, the diagnostics and the ast
    """
    # Parse the source code to get the syntax tree
    parser = Parser(source)
    syntax_tree = parser.parse()

    # Evaluate the syntax tree
    compilation = Compilation(syntax_tree)
    result = compilation.evaluate()

    return {
        'result': result.get_value(),
        'ast': syntax_tree,
        'diagnostics': result.get_diagnostics()
    }


class ConsoleColor:
    """
        Enum containing colors for the console

        Taken from: https://stackoverflow.com/a/287944
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
