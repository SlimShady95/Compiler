from Compiler.Evaluator import Evaluator
from Compiler.Parser import Parser
from Compiler.SyntaxNode import SyntaxNode

def pretty_print(node: SyntaxNode, indent = '', is_last = True):
    """
        Pretty prints the given node and its childs to represent the syntax tree

        :param SyntaxNode node
            The root node to print
        :param string indent
            The indent for the current depth
        :param bool is_last
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

def eval(source: str) -> dict:
    """
        Takes the given source code and evaluates it

        :param string source
            The source code which should be executed
        :return dict
            Returns a dictionary containing the result, the diagnostics and the ast
    """
    parser = Parser(source)
    syntax_tree = parser.parse()
    diagnostics = syntax_tree.get_diagnostics()
    result = None
    if len(diagnostics) == 0:
        evaluator = Evaluator(syntax_tree.get_root())
        result = evaluator.evaluate()

    return {
        'result': result,
        'ast': syntax_tree,
        'diagnostics': diagnostics
    }