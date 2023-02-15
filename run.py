from Compiler.Parser import Parser
from Compiler.SyntaxNode import SyntaxNode

from os import system, name as os_name

def pretty_print(node: SyntaxNode, indent = '', is_last = True):
    marker = '└──' if is_last else '├──'
    print(indent, marker, node.get_kind(), sep='')

    indent += '    ' if is_last else '│   '
    children = node.get_children()
    for child in children:
        pretty_print(child, indent, child == children[-1])


if __name__ == '__main__':
    show_ast = False
    show_diagnostic = True
    while True:
        line = input('> ')

        if line == '#exit':
            break
        
        elif line == '#cls':
            system('cls' if os_name == 'nt' else 'clear')
            continue

        elif line == '#diagnostic':
            show_diagnostic = not show_diagnostic
            continue

        elif line == '#tree':
            show_ast = not show_ast
            print('Displaying syntax tree.' if show_ast else 'Not displaying syntax tree.')
            continue


        parser = Parser(line)
        syntax_tree = parser.parse()
        diagnostics = parser.get_diagnostics()
        if show_diagnostic and len(diagnostics):
            for diagnostic in diagnostics:
                print(diagnostic)
                continue

        if show_ast:
            pretty_print(syntax_tree.get_root())
