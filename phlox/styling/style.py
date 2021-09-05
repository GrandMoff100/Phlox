from ..elements import Element
from .parser import Parser


def parse(string):
    parser = Parser.parser(debug=False)
    return parser.parse(
        string,
        lexer=Parser.lexer(
            debug=False
        )
    )


class Style(Element):
    tag = 'style'

    def style(self, *args, **kwargs):
        if self.children:
            string, *_ = self.children
            new_table = parse(string)
            Element.style_table.update(new_table)
        yield ''
