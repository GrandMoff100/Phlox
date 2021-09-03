from .elements.parser import Parser
from .elements import Element


def render(string):
    parser = Parser.parser()
    page = parser.parse(string, lexer=Parser.lexer())
    elements = page.style()
    print('style_table', Element.style_table)
    return ''.join(elements)
