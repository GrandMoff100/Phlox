from .element import Element


class Div(Element):
    tag = 'div'

    def style(self, *args, **kwargs):
        if style_rule := self.style_rule():
            print(style_rule)
        yield from super().style(*args, **kwargs)
