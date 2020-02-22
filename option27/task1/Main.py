from operator import itemgetter


def sort(_iterable):
    _map = {}
    for x in _iterable:
        if x not in _map.keys():
            _map[x] = 0
        _map[x] += 1
    _map = list(_map.items())
    _map = sorted(_map, key=itemgetter(1))

    prev = _map[0]
    prev_i = 0
    i = 1
    _sorted = []

    for e in _map[1:]:
        if e[1] != prev[1]:
            _sorted += sorted(_map[prev_i:i], key=itemgetter(0))
            prev_i = i
        prev = e
        i += 1
    _sorted += sorted(_map[prev_i:i], key=itemgetter(0))
    return _sorted


_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 3, 6, 3, 7, 23, 7]
m = sort(_list)
print(m)


