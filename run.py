from Compiler.Parser import Parser

if __name__ == '__main__':
    while True:
        line = input('> ')

        parser = Parser(line)
