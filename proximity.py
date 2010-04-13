#!/usr/bin/env python

def euclidean(a, b):
    ''' L2 distance without square root '''
    diff = [(aa - bb) ** 2 for aa, bb in zip(a, b)]
    return sum(diff)


def manhattan(a, b):
    ''' L1 distance '''
    diff = [(aa - bb) for aa, bb in zip(a, b)]
    return sum(diff)
