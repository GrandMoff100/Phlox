from ..utils import StyleTable
from rich.segment import Segment
from rich.style import Style


class Element:
    style_table = StyleTable()

    tag = None
    default_attrs = None

    non_inheritable_attrs = (
        'class',
        'id'
    )

    def __init__(self, attrs=None, children=None):
        if attrs is None:
            attrs = {}
            if self.default_attrs:
                attrs.update(self.default_attrs)
        if children is None:
            children = []
        self.attrs = attrs
        self.children = children

    def __repr__(self):
        return f'<TRMLElement type={self.tag} children={len(self.children)}>'

    @staticmethod
    def create_element(tag, attrs=None, children=None):
        cls = Element.element_tags().get(tag, Element)
        return cls(attrs=attrs, children=children)

    def __rich_console__(self, console, options):
        self.inherit_attrs()
        for elem in self.children:
            if isinstance(elem, str):
                yield Segment(elem, style=Style(
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
                ))
            else:
                yield elem

    @staticmethod
    def registered_elements():
        for subclass in Element.__subclasses__():
            if subclass.tag is not None:
                yield subclass

    @staticmethod
    def element_tags():
        return {subclass.tag: subclass for subclass in Element.registered_elements()}

    def inherit_attrs(self):
        if self.children:
            for child in self.children:
                if isinstance(child, str):
                    continue
                for key in self.attrs:
                    if key not in child.attrs and key not in self.non_inheritable_attrs:
                        child.attrs[key] = self.attrs[key]
                child.inherit_attrs()
