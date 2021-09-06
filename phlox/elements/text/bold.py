from colorama import Style

from ..element import Element


class Bold(Element):
    tag = 'bold'

    async def style(self, *args, **kwargs):
        yield Style.BRIGHT
        async for text in super().style(*args, **kwargs):
            yield text
        yield Style.NORMAL
