#!/usr/bin/env python

def euclidean(a, b):
    ''' L2 distance without square root '''
    d = .0
    for aa, bb in zip(a, b):
        d += (aa - bb) ** 2
    return d


def manhattan(a, b):
    ''' L1 distance '''
    d = .0
    for pair in zip(a, b):
        d += abs(pair[0] - pair[1])
    return d
