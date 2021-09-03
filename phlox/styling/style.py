from ..elements import Element
from .parser import Parser
from ..util import nested_update


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
    styleable = False

    def style(self):
        if self.children:
            elem, *_ = self.children
            text, *_ = elem.style()
            style_table = parse(text)
            Element.style_table = nested_update(
                Element.style_table,
                style_table
            )
        yield ''
