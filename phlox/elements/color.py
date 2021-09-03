from colorama.ansi import Fore, Back
from colored import fg, bg

from .element import Element as TRMLStyle


def is_hex(string):
    return len(string) == 7 and \
        string.startswith('#') and \
        False not in [char.lower() in '1234567890abcdef#' for char in string]


class Color(TRMLStyle):
    tag = 'text'

    def style(self, *args, **kwargs):
        color_head = ''
        if color := self.attrs.get('color', None):
            if color.upper() in dir(Fore):
                color_head += getattr(Fore, color.upper())
            elif is_hex(color):
                color_head += fg(color)

        if on := self.attrs.get('on', None):
            if on.upper() in dir(Back):
                color_head += getattr(Back, on.upper())
            elif is_hex(on):
                color_head += bg(on)

        yield color_head
        yield from super().style(*args, **kwargs)
        yield Fore.RESET
        yield Back.RESET
