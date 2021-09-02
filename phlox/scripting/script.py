from ..elements import Element


class Script(Element):
    tag = 'script'
    styleable = False

    def style(self):
        yield from super().style()
