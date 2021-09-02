from ..elements import Element
from .parser import Parser


def parse(string):
    parser = Parser.parser()
    return parser.parse(
        string,
        lexer=Parser.lexer(
            debug=False
        )
    )


class Style(Element):
    tag = 'style'
    styleable = False

    def style(self):
        if self.children:
            text, *_ = self.children
            style_table = parse(text)
            Element.style_table.update(style_table)
        yield ''
