#!/usr/local/bin/ipython
# coding=utf-8
import math
from os.path import join, realpath
from shutil import copyfile
import numpy as np
import matplotlib.pyplot as plt

n = 200
timesteps = 300
alpha = 0.4

# directories
project_root = realpath(join(__file__, '..', '..'))
images_path = join(project_root, 'figure_scripts', 'images')
figures_path = join(project_root, 'Ch6', 'Figs')
file_string = '1d_noise_%03d.pdf'

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
    ax.set_xticklabels([u"0", u"π/2", u"π", u"3π/2", u"2π"])
    plt.xlim([0.00, 2 * math.pi])
    plt.ylim([-4.5, 4.5])
    # ax.set_xlabel('1000 points between ')
    # ax.set_ylabel('y')

    # ax.set_xticks
    
x = np.linspace(0.00, 2 * math.pi + 0.1, n)
sin = np.sin(x)
noise = np.random.randn(n)
noise[0] = noise[-1] = 0
y = sin + noise

movie_fig = plt.figure(figsize=(4,3))
b_border = 0.1
l_border = 0.035
t_border = 0.01
r_border = 0.03
ax_size = [0+l_border,            0+b_border,            # left, bottom
           1-l_border - r_border, 1-b_border - t_border] # width, height
movie_ax = movie_fig.add_axes(ax_size)

for i in range(timesteps):
    movie_ax.cla()
    plot_series(x, y, movie_ax)
    y = diffuse(y, alpha)
    filename = file_string%i
    print 'Saving frame', filename
    filepath = join(images_path, filename)
    movie_fig.savefig(filepath)

for id_for_figure in (0, 1, 3, 15, 99, 299):
    filename = file_string % id_for_figure
    print("Copying " + filename)
    src = join(images_path, filename)
    dst = join(figures_path, filename)
    copyfile(src,dst)
    