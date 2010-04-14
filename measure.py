# utility function for computing impurity of a given dataset

import math

def cls_err(dataset):
    '''
    Classification Error
        1 - Max( P(Class_k) )
    '''
    freq = {}   # class freq holder

    # for each instance,
    # accumlates the freq of the class of that instance belongs to
    for instance in dataset:
        cls_label = instance.cls
        if freq.has_key(cls_label):
            freq[cls_label] += 1
        else:
            freq[cls_label] = 1.0

    # find max prob
    size     = len(dataset)
    max_prob = .0
    max_cls  = None
    for cls, f in freq.items():
        if f/size > max_prob:
            max_prob = f/size
            max_cls  = cls

    return 1 - max_prob, cls
