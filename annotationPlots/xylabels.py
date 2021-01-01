import pandas as pd, numpy as np, matplotlib.pyplot as plt


array = np.array([0.609, 0.712, 0.493, 1.248, 1.497])
indexes = np.arange(len(array))

fig = plt.figure(figsize=(9, 6), facecolor='.45')
ax = fig.add_subplot()
ax.plot(array, 'yo-', linewidth=2, markerfacecolor='c', markeredgecolor='b')

ax.set_xticks(indexes)
ax.set_yticks(array)
ax.tick_params(direction="inout", color='b', width=2, labelcolor='c', labelsize='small')


ax.set_yticklabels([f"array[{index}]={array[index]:.3f}" for index in array.argsort()],
                    family="monospace")

common_vals = {'fontname': "monospace",
               'fontsize': 12,
               'fontweight': 'bold'
              }
ax.set_xlabel("index", **common_vals)
ax.set_ylabel("array[index]", labelpad=-25, **common_vals)
ax.set_title("an example plot for axes labels and ticks")


ax.legend(["Random Numbers"], loc='upper center')
ax.grid()


index = array.argmin()
ax.annotate("minimum", xy=(index+.05, array[index]),
                       xytext=(index+.15, array[index]),
                       arrowprops=dict(headwidth=4, headlength=4, width=2),
                       horizontalalignment='left',
                       verticalalignment='top'
           )

index = array.argmax()
ax.annotate("maximum", xy=(index-.05, array[index]),
                       xytext=(index-.05 - .7, array[index]),
                       arrowprops=dict(headwidth=4, headlength=4, width=2),
                       horizontalalignment='left',
                       verticalalignment='top'
           )
fig.savefig("figure.png", facecolor=fig.get_facecolor(), edgecolor='none')