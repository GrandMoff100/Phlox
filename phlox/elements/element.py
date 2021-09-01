class Element:
    style_table = {}
    tag = None
    default_attrs = None
    non_inheritable_attrs = [
        'class',
        'id'
    ]

    def __init__(self, attrs=None, children=None, text=None):
        if attrs is None:
            attrs = {}
            if self.default_attrs:
                attrs.update(self.default_attrs)
        if children is None:
            children = []
        self.attrs = attrs
        self.children = children
        self.text = text

    def __repr__(self):
        return f'<TRMLStyle type={self.tag} children={len(self.children)}>'

    @staticmethod
    def create_element(tag, attrs=None, children=None):
        cls = Element.element_tags().get(tag, Element)
        return cls(attrs=attrs, children=children)

    def style(self):
        if self.text:
            yield self.text
        else:
            self.inherit_attrs()
            for child in self.children:
                if isinstance(child, str):
                    yield child
                elif isinstance(child, Element):
                    yield from child.style()


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
                for key in self.attrs:
                    if key not in child.attrs and key not in self.non_inheritable_attrs:
                        child.attrs[key] = self.attrs[key]
                child.inherit_attrs()
