from ..element import Element
from ...styling import parse as parse_stylesheet
from ...scripting import parse as parse_script


async def handle_stylesheet(browser, src):
    content = await browser.fetcher.get(src)
    if isinstance(content, bytes):
        content = content.decode('utf-8')
    newtable = parse_stylesheet(content)
    Element.style_table.update(newtable)


async def handle_script(browser, src):
    content = await browser.fetcher.get(src)
    if isinstance(content, bytes):
        content = content.decode('utf-8')
    script = parse_script(content)
    return script
