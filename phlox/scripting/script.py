from ..elements import Element


class Script(Element):
    tag = 'script'

    def style(self):
        yield from super().style()
