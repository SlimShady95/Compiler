from Compiler.Parser import Parser
from Compiler.SyntaxNode import SyntaxNode

from os import system, name as os_name

def pretty_print(node: SyntaxNode, indent = '', is_last = False):
    marker = '└──' if is_last else '├──'
    print(indent, marker, node.get_kind(), sep='')

    indent += '   ' if is_last else '│   ';
    children = node.get_children()
    for child in children:
        pretty_print(child, indent, children[-1] == child)


if __name__ == '__main__':
    show_ast = False
    while True:
        line = input('> ')

        if line == '#exit':
            exit()

        elif line == '#tree':
            show_ast = not show_ast
            print('Displaying syntax tree.' if show_ast else 'Not displaying syntax tree.')
            continue
        
        elif line == '#cls':
            system('cls' if os_name == 'nt' else 'clear')
            continue

        parser = Parser(line)
        expression = parser.parse()

        if show_ast:
            pretty_print(expression)
