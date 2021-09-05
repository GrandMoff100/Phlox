from ..elements import Element


class Script(Element):
    tag = 'script'

    def style(self, *args, dry=False, **kwargs):
        yield from super().style(*args, **kwargs)
