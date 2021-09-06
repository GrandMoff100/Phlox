from .element import Element


class Break(Element):
    tag = 'br'

    async def style(self, *args, **kwargs):
        yield '\n'
