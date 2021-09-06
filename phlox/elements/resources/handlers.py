from ..elements import Element
from ..styling import parse as parse_stylesheet
from ..scripting import parse as parse_script


async def handle_stylesheet(browser, src):
    content = await browser.fetcher.get(src)
    newtable = parse_stylesheet(content.decode('utf-8'))
    Element.style_table.update(newtable)


async def handle_script(browser, src):
    content = await browser.fetcher.get(src)
    script = parse_script(content.decode('utf-8'))
    return script
