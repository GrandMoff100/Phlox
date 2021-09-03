from ..elements import Element


class Script(Element):
    tag = 'script'
    styleable = False

    def style(self, *args, dry=False, **kwargs):
        yield from super().style(*args, **kwargs)
