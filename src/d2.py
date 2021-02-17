import seaborn as sns
import matplotlib.pyplot  as plt
import numpy as np
import pandas as pd

VIVO_C = ["#415fff"
        , "#6a79ff"
        , "#8d94ff"
        , "#afb0ff"
        , "#D0cdff"
        , "#f2ecff"
        ]

f, ax = plt.subplots()
sns.set_theme()
sns.axes_style("darkgrid")

tips = pd.read_csv('~/Project/pyV/dataset/tips.csv')

sns.set_palette(VIVO_C)


#ax.legend(ncol=2, loc='lower right', frameon=False)
ax.patch.set_facecolor(VIVO_C[5])
ax.grid(True, axis='y', which='major',color='black',
    alpha=0.2)
#ax.set_xticks([])
#ax.axes.get_yaxis().set_visible(True)

g = sns.histplot(data=tips, x="total_bill", hue="sex", 
    bins=35, multiple="stack",
    linewidth=0, shrink=.8)

sns.despine(right=True
    , left=True
    #, top=True
    #, bottom=True
    )

leg = g.legend_
#leg = g.axes.flat[0].get_legend()
leg.set_title('check')
plt.show()
f.savefig("out.png")

