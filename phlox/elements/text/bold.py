from colorama import Style

from ..element import Element


class Bold(Element):
    tag = 'bold'

    def style(self):
        yield Style.BRIGHT
        yield from super().style()
        yield Style.NORMAL
