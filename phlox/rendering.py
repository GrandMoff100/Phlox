import aioconsole
from .elements.parser import Parser


def makepage(string):
    parser = Parser.parser()
    return parser.parse(string, lexer=Parser.lexer())


async def render(string, browser=None):
    content = ''
    page = makepage(string)
    if page:
        async for _ in page.style(dry=True, browser=browser):
            pass
        yields = [text async for text in page.style()]
        content = ''.join(yields)
    await aioconsole.aprint(repr(content))
