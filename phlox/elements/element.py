from collections import defaultdict


class Element:
    style_table = defaultdict(dict)

    tag = None
    styleable = True
    default_attrs = None
    non_inheritable_attrs = (
        'class',
        'id'
    )

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
        return f'<TRMLElement type={self.tag} children={len(self.children)} is_text={bool(self.text)}>'

    @staticmethod
    def create_element(tag, attrs=None, children=None):
        cls = Element.element_tags().get(tag, Element)
        return cls(attrs=attrs, children=children)

    def style(self, *args, **kwargs):
        if self.text:
            yield self.text
        else:
            self.inherit_attrs()
            for child in self.children:
                if isinstance(child, str):
                    yield child
                elif isinstance(child, Element):
                    yield from child.style(*args, **kwargs)

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

    def style_rule(self):
        key = self.style_key()
        return Element.style_table.get(key)
    
    def style_key(self):
        def segments():
            if self.tag:
                yield self.tag
            if self.attrs.get('class'):
                yield self.attrs.get('class')
        return tuple(segments())

    
