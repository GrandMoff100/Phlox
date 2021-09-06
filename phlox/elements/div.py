from .element import Element


class Div(Element):
    tag = 'div'

    async def style(self, *args, **kwargs):
        async for text in super().style(*args, **kwargs):
            yield text
