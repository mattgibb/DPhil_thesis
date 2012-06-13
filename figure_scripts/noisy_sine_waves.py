#!/usr/local/bin/ipython

import math
from os.path import join
import numpy as np
import matplotlib.pyplot as plt

images_dir = join(__file__, '../../Ch6/Figs/')

n = 200
alpha = 0.4

def diffuse(series, alpha):
    # calculate nearest neighbour diffusion term with Dirichlet BCs
    # y_(n-1) - 2y_n + y_(n+1)
    delta = np.concatenate((
        [0],
        series[0:-2] - 2 * series[1:-1] + series[2:],
        [0]
    ))
    return series + alpha * delta

def plot_series(x,y,ax):
    ax.plot(x, np.sin(x))
    ax.plot(x, y)
    ax.set_ylim([-5,5])
    plt.xticks( np.linspace(0.00, 2 * math.pi, 5) )
    # ax.set_xlabel('1000 points between ')
    # ax.set_ylabel('y')

    # ax.set_xticks
    
x = np.linspace(0.00, 2 * math.pi + 0.1, n)
sin = np.sin(x)
noise = np.random.randn(n)
noise[0] = noise[-1] = 0
y = sin + noise

movie_fig = plt.figure()
movie_ax = movie_fig.add_subplot(111)
for i in range(100):
    movie_ax.cla()
    plot_series(x, y, movie_ax)
    y = diffuse(y, alpha)
    filename = '_tmp%03d.png'%i
    print 'Saving frame', filename
    movie_fig.savefig(filename)
