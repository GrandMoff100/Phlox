
def nested_update(old, new):
    for k, v in new.items():
        if isinstance(old.get(k), dict) and isinstance(v, dict):
            old.update({k: nested_update(old.get(k), v)})
        else:
            old.update({k: v})
    return old
