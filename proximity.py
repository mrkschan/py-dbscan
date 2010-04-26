#!/usr/bin/env python

def euclidean(a, b):
    ''' L2 distance without square root '''
    diff = [(aa - bb) ** 2 for aa, bb in zip(a, b)]
    return sum(diff)


def manhattan(a, b):
    ''' L1 distance '''
    diff = [(aa - bb) for aa, bb in zip(a, b)]
    return sum(diff)

cache = {}
def build_cache(dataset, distance=euclidean):
    ''' build distance cache.
        each vector will compute the distance with others
        distance from others are sorted ASC '''
    global cache
    for a in dataset:
        pairs = [(b, distance(a.tuple, b.tuple)) for b in dataset if a != b]
        cache[a] = sorted(pairs, key=lambda p: p[1])
