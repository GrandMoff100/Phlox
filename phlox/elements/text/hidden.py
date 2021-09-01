from ..element import Element


class Hidden(Element):
    tag = 'hide'

    def style(self):
        if self.attrs.get('hidden', 'true') == 'true':
            content = ''.join(super().style())
            for i, char in enumerate(content):
                if char not in '\n':
                    yield ' '
                else:
                    yield char
        else:
            yield from super().style()
