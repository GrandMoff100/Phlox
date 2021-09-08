from .element import Element
from rich.text import Text as rText
from rich.style import Style


class Text(Element):
    tag = 'text'

    def __rich__(self):
        if self.children:
            if isinstance(self.children[0], str):
                return rText(self.children[0], 
                    style=Style(
                        bold=self.attrs.get('bold'),
                        dim=self.attrs.get('dim'),
                        italic=self.attrs.get('italic'),
                        blink=self.attrs.get('blink'),
                        blink2=self.attrs.get('fast_blink'),
                        underline=self.attrs.get('underline'),
                        underline2=self.attrs.get('double_underline'),
                        color=self.attrs.get('color'),
                        bgcolor=self.attrs.get('on_color'),
                        overline=self.attrs.get('overline'),
                        conceal=self.attrs.get('conceal')
                    ),
                    justify=self.attrs.get('justify'),
                    overflow=self.attrs.get('overflow'),
                    no_wrap=self.attrs.get('no_wrap'),
                    end=''
                )
        
