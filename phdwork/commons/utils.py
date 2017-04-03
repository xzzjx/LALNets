'''
Essential functions commonly used in scripts.

'''

import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec


def plot_class_means(nb_classes, nb_clusters, est, test, cmap=None, boundary=None, sort=False, transpose=False, ax=None):
    if ax is None:
        ax = plt.gca()

    n,h,w,d = test.shape
    if boundary is None:
        boundary = range(n)

    if cmap is None:
        cmap = cm.jet

    if transpose:
        img = np.zeros((h*nb_classes,w*nb_clusters))
    else:
        img = np.zeros((h*nb_clusters,w*nb_classes))
    imgSorted = np.zeros_like(img)
    ind = np.zeros((nb_clusters, nb_classes))
    for i in range(nb_clusters):
        for j in range(nb_classes):
            a = test[boundary,:][est[boundary]==j+nb_classes*i]
            b = a.shape[0]
            if b == 0:
                a = np.zeros((h,w))
            else:
                a = a.mean(axis=0).reshape(h,w)
            ind[i,j] = b
            if transpose:
                img[j*h:(j+1)*h,i*w:(i+1)*w] = a
            else:
                img[i*h:(i+1)*h,j*w:(j+1)*w] = a

    for i in range(nb_clusters):
        for j in range(nb_classes):
            if sort:
                k = ind.argsort(axis=0)[::-1][i,j]
            else:
                k = i
            if transpose:
                imgSorted[j*h:(j+1)*h,i*w:(i+1)*w] = img[j*h:(j+1)*h,k*w:(k+1)*w]
            else:
                imgSorted[i*h:(i+1)*h,j*w:(j+1)*w] = img[k*h:(k+1)*h,j*w:(j+1)*w]

    fig = ax.imshow(imgSorted,cmap=cmap, interpolation='bicubic')

    ax.axis('off')
    ax.grid('off')