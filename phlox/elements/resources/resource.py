from ..element import Element
from .handlers import (
    handle_stylesheet,
    handle_script
)


class Resource(Element):
    tag = 'resource'
    types = {
        '.tss': 'stylesheet',
        '.ps': 'script'
    }
    handlers = {
        'stylesheet': handle_stylesheet,
        'script': handle_script
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def style(self, *args, browser=None, dry=False, **kwargs):
        if (src := self.attrs.get('src')):
            if (_type := self.attrs.get('type')) is None:
                for ext, value in self.types.items():
                    if src.endswith(ext):
                        _type = value
                        break
            if _type is not None:
                handler = self.handlers.get(_type, self.handler_not_found)
                if dry is False:
                    handler(browser, src)

    def handler_not_found(self, browser, src):
        print(f"Handler not specified and could not be guess for {src!r}")
