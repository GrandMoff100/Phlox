from ..element import Element
from termcolor import colored


class Blink(Element):
    tag = 'blink'

    def style(self):
        yield colored(''.join(super().style()), attrs=['blink'])
