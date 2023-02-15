from Compiler.SyntaxKind import SyntaxKind


class SyntaxFacts:
    operators = {
        SyntaxKind.PLUS_TOKEN: 1,
        SyntaxKind.MINUS_TOKEN: 1,
        SyntaxKind.STAR_TOKEN: 2,
        SyntaxKind.SLASH_TOKEN: 2,
    }

    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int:
        return SyntaxFacts.operators.get(kind, 0)
