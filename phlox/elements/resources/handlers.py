from ..elements import Element
from ..styling import parse as parse_stylesheet
from ..scripting import parse as parse_script


def handle_stylesheet(browser, src):
    content = browser.requester.get(src)
    newtable = parse_stylesheet(content)
    Element.style_table.update(newtable)


def handle_script(browser, src):
    content = browser.requester.get(src)
    script = parse_script(content)
    return script
