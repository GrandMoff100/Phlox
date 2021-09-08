from .element import Element
from rich.measure import Measurement


class Div(Element):
    tag = 'div'

    def __rich_measure__(self, console, options):
        return Measurement(
            minimum=self.style_table.get_style('min_width'),
            maximum=self.style_table.get_style('max_width')
        )

