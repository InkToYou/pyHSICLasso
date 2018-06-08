#!usr/bin/env python
# coding: utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from builtins import range

import seaborn as sns
import pandas as pd
from future import standard_library
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.cluster.hierarchy import  dendrogram

microarray_cmap = LinearSegmentedColormap('microarray', {
    'red': [(0.0, 1.0, 1.0), (0.5, 0.2, 0.2), (1.0, 0.0, 0.0)],
    'green': [(0.0, 0.0, 0.0), (0.5, 0.2, 0.2), (1.0, 1.0, 1.0)],
    'blue': [(0.0, 0.0, 0.0), (0.5, 0.2, 0.2), (1.0, 0.0, 0.0)],
})

standard_library.install_aliases()

def plot_heatmap(X, row_linkage,featname):
    df = pd.DataFrame(X)
    df.index = featname
    cg = sns.clustermap(df,row_linkage=row_linkage,method='ward',cmap=microarray_cmap)
    cg.ax_heatmap.set_xticklabels("")
    plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    plt.setp(cg.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
    plt.title('Heatmap')
    plt.show()

def plot_dendrogram(linkage,featname):
    dendrogram(linkage,labels=featname)
    plt.title("Dendrogram")
    plt.show()

def plot_path(path, beta, A):
    t = path.sum(0)
    plt.title("HSICLasso Result")
    plt.xlabel("lambda")
    plt.ylabel("cofficients")
    for ind in range(len(A)):
        plt.plot(t, path[A[ind], :], label="{}".format(A[ind] + 1))
    plt.legend()
    plt.show()
