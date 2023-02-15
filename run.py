from Compiler.Helper import eval, pretty_print

from os import system, name as os_name

if __name__ == '__main__':
    # Flags for showing/not showing the syntax tree and diagnostics
    show_ast = False
    show_diagnostic = True

    # As long as the user does not enter #exit we will run the loop and execute 
    # the given code each time
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
        result = eval(line)

        # Display all diagnostics
        if show_diagnostic:
            for diagnostic in result.get('diagnostics'):
                print(diagnostic)

        # Display syntax tree
        if show_ast:
            pretty_print(result.get('ast').get_root())

        # Display result :)
        print('-->', result.get('result'))
