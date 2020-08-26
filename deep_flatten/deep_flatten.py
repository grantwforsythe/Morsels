from collections.abc import Iterable


def deep_flatten(obj):
    for val in obj:
        if not isinstance(val, Iterable) or isinstance(val, str):
            yield val
        else:
            yield from deep_flatten(val)

if __name__ == '__main__':
    print(list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])))
    print(list(deep_flatten([[1, [2, 3]], 4, 5])))
    print(sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})))
    print(list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']])))