#!/usr/bin/env python

import dbscan

cls_idx = 4

dataset = []
with open('dataset/iris/iris.data') as data_f:
    for l in data_f.readlines():
        r = l.strip().split(',')
        for i in xrange(0, cls_idx):
            r[i] = float(r[i])
        dataset.append(dbscan.data(r, cls_idx))
    data_f.close()

for k in xrange(1, 6):
    for sd_away in xrange(1, 5):
        for d in dataset: d.reset()

        kdist   = dbscan.k_distance(dataset, k, sd_away)
        cluster = dbscan.dbscan(dataset, kdist, k)
        print 'k:', k, 'kdist:', kdist, 'cluster size:', len(cluster)
