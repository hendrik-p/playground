#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = sys.argv[1]
    a = np.genfromtxt(path)
    if len(a.shape) > 1:
        _, nb_cols = a.shape
        for i in range(nb_cols):
            plt.plot(a[:, i])
    else:
        plt.plot(a)
    plt.show()
