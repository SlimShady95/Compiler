from Compiler.SyntaxKind import SyntaxKind


class SyntaxFacts:
    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int:
        if kind in [SyntaxKind.PLUS_TOKEN, SyntaxKind.MINUS_TOKEN]:
            return 1
        elif kind in [SyntaxKind.STAR_TOKEN, SyntaxKind.SLASH_TOKEN]:
            return 2

        return 0
