from ..elements import Element
#  from .parser import Parser


def parse(string):
    pass


class Script(Element):
    tag = 'script'

    async def style(self, *args, dry=False, **kwargs):
        yield ''
