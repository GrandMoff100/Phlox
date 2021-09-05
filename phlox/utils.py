
def nested_update(old, new):
    for k, v in new.items():
        if isinstance(v, dict) and isinstance(old.get(k, None), dict):
            old[k] = nested_update(old.get(k), v)
        else:
            old[k] = v
    return old


class StyleTable(dict):
    def get_style(self, tag, class_=None, state=None):
        if class_ is None:
            class_ = 'default'
        if state is None:
            state = 'normal'
        return self.get(tag, {}).get(class_, {}).get(state, None)

    def update(self, obj):
        super().update(nested_update(self, obj))


class Document:
    def __init__(self, page):
        self.page = page

    def get_element_by_id(self, id):
        pass

    def get_elements_by_tag(self, tag):
        pass

    def get_elements_by_class(self, class_):
        pass

