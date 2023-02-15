from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxNode import SyntaxNode


class SyntaxToken(SyntaxNode):
    _kind = None
    _position = -1
    _text = ''
    _value = None

    def __init__(self, kind: SyntaxKind, position: int, text: str, value) -> None:
        self._kind = kind
        self._position = position
        self._text = text
        self._value = value

    def get_kind(self) -> SyntaxKind:
        return self._kind

    def get_position(self) -> int:
        return self._position

    def get_text(self) -> str:
        return self._text

    def get_value(self):
        return self._value

    def get_children(self):
        return []

    def __repr__(self) -> str:
        return f'Token(kind={self._kind}, position={self._position}, text={self._text}, value={self._value})'

    def __str__(self) -> str:
        return self.__repr__()
