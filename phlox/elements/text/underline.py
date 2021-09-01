from ..element import Element
from termcolor import colored


class Underline(Element):
    tag = 'underline'

    def style(self):
        yield colored(''.join(super().style()), attrs=['underline'])
