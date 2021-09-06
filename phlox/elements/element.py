from ..utils import StyleTable


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

    async def style(self, *args, **kwargs):
        await self.inherit_attrs()
        for child in self.children:
            if isinstance(child, str):
                yield child
            elif isinstance(child, Element):
                async for text in child.style(*args, **kwargs):
                    yield text

    @staticmethod
    def registered_elements():
        for subclass in Element.__subclasses__():
            if subclass.tag is not None:
                yield subclass

    @staticmethod
    def element_tags():
        return {subclass.tag: subclass for subclass in Element.registered_elements()}

    async def inherit_attrs(self):
        if self.children:
            for child in self.children:
                if isinstance(child, str):
                    continue
                for key in self.attrs:
                    if key not in child.attrs and key not in self.non_inheritable_attrs:
                        child.attrs[key] = self.attrs[key]
                await child.inherit_attrs()
