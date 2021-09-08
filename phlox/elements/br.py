from .element import Element
from rich.console import NewLine


class Break(Element):
    tag = 'br'

    def __rich__(self):
        return NewLine()
