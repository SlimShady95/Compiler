from Compiler.Syntax.Helper import evaluate, pretty_print, ConsoleColor

from os import system, name as os_name

if __name__ == '__main__':
    # Flags for showing/not showing the syntax tree and diagnostics
    show_ast = False
    show_diagnostic = True

    # As long as the user does not enter #exit we will run the loop and execute 
    # the given cod
    # e each time
    while True:
        line = input('> ')
        if line == '#exit':
            break
        
        # Clear the console
        elif line == '#cls':
            system('cls' if os_name == 'nt' else 'clear')
            continue

        # Turn on/off diagnostics
        elif line == '#diagnostic':
            show_diagnostic = not show_diagnostic
            print('Displaying diagnostics.' if show_diagnostic else 'Not showing diagnostics.')
            continue

        # Turn on/off showing the syntax tree
        elif line == '#tree':
            show_ast = not show_ast
            print('Displaying syntax tree.' if show_ast else 'Not displaying syntax tree.')
            continue

        # Turn the line of code into its tokens and evaluate it
        result = evaluate(line)

        # Display all diagnostics
        if show_diagnostic:
            print()
            for diagnostic in result.get('diagnostics'):
                print(diagnostic)

                span = diagnostic.get_span()
                prefix = line[0:span.get_start()]
                error = line[span.get_start():span.get_end()]
                suffix = line[span.get_end():]
                print(f'\t{prefix}{ConsoleColor.RED}{error}{ConsoleColor.END}{suffix}')
                print(f'\t{" "*span.get_start()}{"^"*span.get_length()}')

        # Display syntax tree
        if show_ast:
            pretty_print(result.get('ast').get_root())

        # Display result :)
        print('-->', result.get('result'))
