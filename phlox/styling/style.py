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
    styleable = False

    def style(self, *args, **kwargs):
        if self.text:
            yield self.text
        elif self.children:
            elem, *_ = self.children
            text, *_ = elem.style(*args, **kwargs)
            style_table = parse(text)
            for tag, style in style_table.items():
                Element.style_table[tag].update(style)
