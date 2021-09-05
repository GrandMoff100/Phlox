from ..elements import Element
from .parser import Parser


def parse(string):
    pass


class Script(Element):
    tag = 'script'

    def style(self, *args, dry=False, **kwargs):
        yield from super().style(*args, **kwargs)
