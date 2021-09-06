from ..element import Element


class Hidden(Element):
    tag = 'hide'

    async def style(self, *args, **kwargs):
        if self.attrs.get('hidden', 'true') == 'true':
            content = ''.join(super().style(*args, **kwargs))
            for i, char in enumerate(content):
                if char not in '\n':
                    yield ' '
                else:
                    yield char
        else:
            async for text in super().style(*args, **kwargs):
                yield text
