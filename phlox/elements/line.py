from .element import Element


class LineDivider(Element):
    tag = 'line'

    def style(self):
        print(self.children)
        print(self.text)
        yield ''