from .text import Text


class Link(Text):
    tag = 'a'

    def __rich__(self):
        if text := super().__rich__():
            if target := self.attrs.get('href'):
                if self.children:
                    if isinstance(self.children[0], str):
                        text.style = text.style.chain(Style(link=target))
            return text