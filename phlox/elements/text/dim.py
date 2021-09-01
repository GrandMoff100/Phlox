from ..element import Element
from colorama import Style


class Dim(Element):
    tag = 'dim'

    def style(self):
        yield Style.DIM
        yield from super().style()
        yield Style.NORMAL
