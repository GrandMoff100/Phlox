from .element import Element


class LineDivider(Element):
    tag = 'line'

    async def style(self, *args, **kwargs):
        yield ''
