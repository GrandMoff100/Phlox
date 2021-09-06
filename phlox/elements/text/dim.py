from ..element import Element
from colorama import Style


class Dim(Element):
    tag = 'dim'

    async def style(self, *args, **kwargs):
        yield Style.DIM
        async for text in super().style(*args, **kwargs):
            yield text
        yield Style.NORMAL
