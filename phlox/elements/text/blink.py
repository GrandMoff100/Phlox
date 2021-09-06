from ..element import Element
from termcolor import colored


class Blink(Element):
    tag = 'blink'

    async def style(self, *args, **kwargs):
        yield colored(''.join([item async for item in super().style(*args, **kwargs)]), attrs=['blink'])
