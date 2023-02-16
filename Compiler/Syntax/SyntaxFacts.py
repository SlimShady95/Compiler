from Compiler.Syntax.SyntaxKind import SyntaxKind


class SyntaxFacts:
    binary_operators = {
        SyntaxKind.PLUS_TOKEN: 1,
        SyntaxKind.MINUS_TOKEN: 1,
        SyntaxKind.STAR_TOKEN: 2,
        SyntaxKind.SLASH_TOKEN: 2,
    }

    unary_operators = {
        SyntaxKind.PLUS_TOKEN: 3,
        SyntaxKind.MINUS_TOKEN: 3
    }

    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int:
        return SyntaxFacts.binary_operators.get(kind, 0)

    @staticmethod
    def get_unary_operator_precedence(kind: SyntaxKind) -> int:
        return SyntaxFacts.unary_operators.get(kind, 0)
