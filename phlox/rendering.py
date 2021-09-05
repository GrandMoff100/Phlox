from .elements.parser import Parser


def render(string):
    parser = Parser.parser()
    page = parser.parse(string, lexer=Parser.lexer())
    content = ''.join(page.style())
    return content
