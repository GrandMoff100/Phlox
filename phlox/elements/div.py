from .element import Element


class Div(Element):
    tag = 'div'

    def style(self, *args, **kwargs):
        yield from super().style(*args, **kwargs)