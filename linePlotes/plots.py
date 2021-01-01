import numpy as np, pandas as pd, matplotlib.pyplot as plt


numbers = [0.6092181 , 0.71235272, 0.49331146, 1.248927  , 1.49723557]
linestyles = ['-', '--', '-.', ':', 'dashdot']
drawstyles = ['default', 'steps', 'steps-pre', 'steps-mid', 'steps-post']
colors, bgcolors, markers = 'rmgbw', 'cywwk', '^o+*<>'
stylings = zip(linestyles, drawstyles, colors, bgcolors, markers)
fig, axes = plt.subplots(3, 2, sharex=True, sharey=True)
for i, (ls, ds, c, bg, m) in enumerate(stylings):
    fig.axes[i].plot(numbers, ls=ls, ds=ds, marker=m, color=c)
    fig.axes[i].legend([ds], loc='upper left')
    fig.axes[i].set_facecolor(bg)
fig.axes[3].set_facecolor('.75')
fig.delaxes(axes[-1, -1])
fig.suptitle("Better Exmaple", fontsize=12, fontweight='bold')