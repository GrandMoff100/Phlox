import os
import aioconsole

from urllib.parse import urlparse

from .elements.parser import Parser
from .browser import Browser


def makepage(string):
    parser = Parser.parser()
    return parser.parse(string, lexer=Parser.lexer())


def makebrowser(cwd, env):
    return Browser(cwd, env)


async def style(page, browser, *args, **kwargs):
    if page:
        async for _ in page.style(*args, browser=browser, **kwargs):
            pass
        yields = [text async for text in page.style(*args, browser=browser, **kwargs)]
        content = ''.join(yields)
        return content


async def prestyle(page, browser):
    return await style(page, dry=True, browser=browser)


def path_info(uri):
    if (url := urlparse(uri)).scheme != "":
        if url.path == '' and not uri.endswith('/'):
            uri += '/'
    return os.path.split(uri)


async def get_index(browser, index):
    string = await browser.fetcher.get(index)
    if isinstance(string, bytes):
        return string.decode('utf-8')
    return string


async def render(uri, env=None):
    if env is None:
        env = {}
    env.update(os.environ)

    cwd, index = path_info(uri)
    browser = makebrowser(cwd, env)
    string = await get_index(browser, index)
    print(repr(string))
    page = makepage(string)

    await prestyle(page, browser)
    content = await style(page, browser)
    await aioconsole.aprint('Rendering')
    await aioconsole.aprint(repr(content))
