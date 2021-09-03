from colorama import Style

from ..element import Element


class Bold(Element):
    tag = 'bold'

    def style(self, *args, **kwargs):
        yield Style.BRIGHT
        yield from super().style(*args, **kwargs)
        yield Style.NORMAL
