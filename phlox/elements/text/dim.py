from ..element import Element
from colorama import Style


class Dim(Element):
    tag = 'dim'

    def style(self, *args, **kwargs):
        yield Style.DIM
        yield from super().style(*args, **kwargs)
        yield Style.NORMAL
