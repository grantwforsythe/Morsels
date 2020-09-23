from collections.abc import Iterable


def deep_flatten(obj):
    for val in obj:
        if not isinstance(val, Iterable) or isinstance(val, str):
            yield val
        else:
            yield from deep_flatten(val)
