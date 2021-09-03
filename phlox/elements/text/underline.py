from ..element import Element
from termcolor import colored


class Underline(Element):
    tag = 'underline'

    def style(self, *args, **kwargs):
        yield colored(''.join(super().style(*args, **kwargs)), attrs=['underline'])
