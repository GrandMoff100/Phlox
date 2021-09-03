from .element import Element


class LineDivider(Element):
    tag = 'line'

    def style(self, *args, **kwargs):
        print(self.children)
        print(self.text)
        yield ''