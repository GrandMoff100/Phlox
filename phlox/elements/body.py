from .element import Element


class Body(Element):
    tag = 'body'

    async def style(self, *args, **kwargs):
        async for text in super().style(*args, **kwargs):
            yield text
