from .elements.parser import Parser


def render(string):
    parser = Parser.parser()
    page = parser.parse(string, lexer=Parser.lexer())

    for _ in page.style(dry=True):
        pass

    content = ''.join(page.style())
    return content
