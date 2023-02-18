from Compiler.Binding.BoundNode import BoundNode
from Compiler.Binding.BoundNodeKind import BoundNodeKind


class BoundExpression(BoundNode):
    def get_kind(self) -> BoundNodeKind:
        raise NotImplementedError('Can not call abstract method.')

    def get_type(self) -> BoundNodeKind:
        raise NotImplementedError('Can not call abstract method.')

    def get_children(self) -> list:
        return []