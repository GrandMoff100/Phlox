from ..element import Element
from termcolor import colored


class Blink(Element):
    tag = 'blink'

    def style(self, *args, **kwargs):
        yield colored(''.join(super().style(*args, **kwargs)), attrs=['blink'])
