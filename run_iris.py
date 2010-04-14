#!/usr/bin/env python

import dbscan, measure
import copy

cls_idx = 4

dataset = []
with open('dataset/iris/iris.data') as data_f:
    for l in data_f.readlines():
        r = l.strip().split(',')
        for i in xrange(0, cls_idx):
            r[i] = float(r[i])
        dataset.append(dbscan.data(r, cls_idx))
    data_f.close()


# normalize all dimension scale to range float(0, 1)
mins = [copy.deepcopy(min(dataset, key=lambda d: d.tuple[i])) for i in xrange(0, cls_idx)]
maxs = [copy.deepcopy(max(dataset, key=lambda d: d.tuple[i])) for i in xrange(0, cls_idx)]

for d in dataset:
    for i in xrange(0, cls_idx):
        d.tuple[i] = float(d.tuple[i] - mins[i].tuple[i]) / (maxs[i].tuple[i] - mins[i].tuple[i])


# print all combination of k and sd
for k in xrange(2, 10):
    for sd_away in xrange(0, 5):
        try:
            kdist = dbscan.k_distance(dataset, k, sd_away)
        except:
            print 'kdist anchor out of range, skipped'
            print
            continue

        cluster = dbscan.dbscan(dataset, kdist, k)
        if len(cluster) == 0:
            print 'k:', k, 'sd:', sd_away, 'kdist:', kdist, 'no. of cluster:', len(cluster)
            print
            continue

        cc = [measure.cls_err(c) for c in cluster]
        errs = []
        clss = []
        for err, cls in cc:
            errs.append(err)
            clss.append(cls)
        cp = [len(c) for c in cluster]

        print 'k:', k, 'sd:', sd_away, 'kdist:', kdist, 'no. of cluster:', len(cluster)
        for i in xrange(0, len(cluster)):
            print 'cluster:', i, 'no. of pt. in cluster:', cp[i], 'impurity (classification error):', errs[i], 'majority:', clss[i]
        print 'mean impurity:', float(sum(errs)) / len(errs), 'sum of pt.:', sum(cp)
        print
