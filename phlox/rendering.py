import os

from urllib.parse import urlparse

from .elements.parser import Parser
from .browser import Browser


def makepage(string):
    parser = Parser.parser()
    return parser.parse(string, lexer=Parser.lexer())


def makebrowser(cwd, env):
    return Browser(cwd, env)


def path_info(uri):
    if (url := urlparse(uri)).scheme != "":
        if url.path == '' and not uri.endswith('/'):
            uri += '/'
    return os.path.split(uri)


def get_index(browser, index):
    string = browser.fetcher.get(index)
    if isinstance(string, bytes):
        return string.decode('utf-8')
    return string


def render(uri, env=None):
    if env is None:
        env = {}
    env.update(os.environ)

    cwd, index = path_info(uri)
    browser = makebrowser(cwd, env)
    string = get_index(browser, index)
    page = makepage(string)

    browser.webpage.print(page)
    browser.webpage.print('Rendering')
