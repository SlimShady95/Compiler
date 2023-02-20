from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxNode import SyntaxNode
from Compiler.Type.TextSpan import TextSpan


class SyntaxToken(SyntaxNode):
    """
        Container for a syntax token
    """

    # The kind of the token
    _kind = None

    # The position of the token inside the source code
    _position = -1

    # The span of the token
    _span = None

    # The actual text of the token in the source code
    _text = ''

    # The value of the token
    _value = None

    def __init__(self, kind: SyntaxKind, position: int, text: str, value: object) -> None:
        """
            Sets up all properties

            :param kind: SyntaxKind
                The kind of token this is
            :param position: int
                The position inside the source code
            :param text: str
                The actual text inside the source code
            :param value: object
                The value of the token
        """
        self._kind = kind
        self._position = position
        self._span = TextSpan(self._position, len(text))
        self._text = text
        self._value = value

    def get_kind(self) -> SyntaxKind:
        """
            Returns the kind of the token

            :return SyntaxKind
                Returns the kind of the token
        """
        return self._kind

    def get_position(self) -> int:
        """
            Returns the position inside the source code

            :return int
                Returns the position inside the source code
        """
        return self._position

    def get_span(self) -> TextSpan:
        """
            Returns the text span of the token

            :return TextSpan
                Returns the text span of the token
        """
        return self._span

    def get_text(self) -> str:
        """
            Returns the actual text inside the source code

            :return str
                Returns the actual text inside the source code
        """
        return self._text

    def get_value(self) -> object:
        """
            Returns the value of the token

            :return object
                Returns the value of the token
        """
        return self._value

    def get_children(self) -> list:
        """
            Returns a list containing all children

            :return list
                Returns a list containing all children
        """
        return []

    def __repr__(self) -> str:
        """
            Returns the str representation of this token

            :return str
                Returns the str representation of this token
        """
        return f'Token(kind={self._kind}, position={self._position}, text={self._text}, value={self._value})'

    def __str__(self) -> str:
        """
            Returns the str representation of this token

            :return str
                Returns the str representation of this token
        """
        return self.__repr__()
