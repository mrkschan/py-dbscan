#!/usr/bin/env python

import proximity
import math


class data:
    ''' data wrapper '''
    CORE, BORDER, NOISE = 0, 1, 2

    def __init__(self, tuple=None, target_cls_idx=None):
        if tuple is not None and target_cls_idx is not None:
            self.cls     = tuple[target_cls_idx]
            self.tuple   = tuple[:target_cls_idx] + tuple[target_cls_idx+1:]
            self.label   = data.NOISE
            self.visited = False

    def reset(self):
        self.label   = data.NOISE
        self.visited = False


def k_distance(dataset, k, sd_away, distance=proximity.euclidean):
    ''' compute the k-distance as radius for dbscan.
        k-distance is obtained by several standard deviation away from mean (sd) '''
    kdist = []

    for a in dataset:
        dist = [
            distance(a.tuple, b.tuple) \
            for b in dataset if a != b
        ]
        dist.sort()
        kdist.append(dist[k])

    kdist.sort()

    size = len(kdist)
    mean = sum(kdist) / float(size)
    diff = [(d - mean) ** 2 for d in kdist]
    sd   = math.sqrt(sum(diff) / float(size - 1))

    anchor = mean + (sd * sd_away)

    print mean, sd, anchor,

    last = None
    for d in reversed(kdist):
        if d > anchor and last is None:
            last = d
        elif d < anchor and last is not None:
            return last
    raise Exception('sd too far away from mean')


def find_neighbour(instance, dataset, radius, distance):
    ''' find all neighbour within radius '''
    r = radius ** 2
    neighbour = [
        d for d in dataset \
        if instance != d and r >= distance(instance.tuple, d.tuple)
    ]

    return neighbour


def dbscan(dataset, radius, minPt, distance=proximity.euclidean):
    ''' dataset is a list of data wrapper '''
    cluster = []

    for instance in dataset:
        # skip processed
        if instance.visited == True: continue

        instance.visited = True
        neighbour = find_neighbour(instance, dataset, radius, distance)

        if minPt > len(neighbour):
            instance.label = data.NOISE
        else:
            # core point
            c = neighbour[:] + [instance]
            q = neighbour[:]
            cluster.append(c)

            while len(q) > 0:
                check_instance = q.pop()
                neighbour = find_neighbour(check_instance, dataset, radius, distance)

                check_instance.visited = True
                if minPt > len(neighbour):
                    # not core, border
                    check_instance.label = data.BORDER
                else:
                    # core, expand
                    check_instance.label = data.CORE
                    for n in neighbour:
                        if n not in c:
                            c.append(n)
                            q.append(n)

    return cluster
