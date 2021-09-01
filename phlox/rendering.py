from .elements.parser import Parser


def style(string):
    parser = Parser.parser()
    page = parser.parse(string, lexer=Parser.lexer())
    elements = page.style()
    return ''.join(elements)
