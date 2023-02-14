from Compiler.Lexer import Lexer
from Compiler.SyntaxKind import SyntaxKind

class Parser:
    _lexer = None

    def __init__(self, text: str) -> None:
        self._lexer = Lexer(text)
        
        while True:
            token = self._lexer.next_token()
            if (token.get_kind() == SyntaxKind.END_OF_FILE_TOKEN):
                break    
                
            print(token)


