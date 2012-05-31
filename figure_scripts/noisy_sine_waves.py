import math
from os.path import join
import numpy as np
import matplotlib.pyplot as plt

images_dir = join(__file__, '../../Ch6/Figs/')

n = 200

def diffuse(series):
    return np.concatenate((series[0:1], 0.5 * (series[0:-2] + series[2:]), series[-1:]))

def plot_series(x,y,ax):
    ax.plot(x, np.sin(x))
    ax.plot(x, y)
    plt.xticks( np.linspace(0.00, 2 * math.pi, 5) )
    # ax1.set_xlabel('1000 points between ')
    # ax1.set_ylabel('y')

    # ax.set_xticks
    
x = np.linspace(0.00, 2 * math.pi + 0.1, n)
sin = np.sin(x)
noise = np.random.randn(n)
y = sin + noise
fig = plt.figure()
plot_series(x, y, fig.add_subplot(221))
y = diffuse(y)
plot_series(x, y, fig.add_subplot(222))
y = diffuse(y)
plot_series(x, y, fig.add_subplot(223))
y = diffuse(y)
plot_series(x, y, fig.add_subplot(224))
plt.show()
