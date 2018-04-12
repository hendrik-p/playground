#!/usr/bin/env python
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def get_colormap(n):
    return plt.cm.get_cmap('gist_ncar', n)

def reduce_data(data, labels, nb_labels=40):
    #label_sample = random.sample(np.unique(labels), nb_labels)
    label_sample = range(nb_labels)
    label_map = {l : i for i, l in enumerate(label_sample)}
    new_data = []
    new_labels = []
    for i in range(data.shape[0]):
        label = labels[i]
        if label in label_sample:
            new_data.append(data[i])
            new_labels.append(label_map[label])
    return np.array(new_data), new_labels

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    colors = None
    if len(sys.argv) > 2:
        label_path = sys.argv[2]
        labels = [int(s.strip()) for s in open(label_path)]
        data, labels = reduce_data(data, labels)
        nb_labels = len(np.unique(labels))
        cmap = get_colormap(nb_labels)
        colors = [cmap(l) for l in labels]
    plt.scatter(data[:, 0], data[:, 1], c=colors)
    plt.show()
