from ..elements import Element
from .parser import Parser


class Script(Element):
    tag = 'script'

    def style(self, *args, dry=False, **kwargs):
        yield from super().style(*args, **kwargs)
