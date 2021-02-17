import seaborn as sns
import matplotlib.pyplot  as plt
import numpy as np
import pandas as pd

DIR = '~/Project/pyV'
f, ax = plt.subplots()

sns.set_theme()
#sns.set_style("ticks")

#tips = sns.load_dataset("tips", cache=True)
tips = pd.read_csv(DIR + '/dataset/tips.csv')

vivo_c = ["#d0cdff", "#415fff", "#FF4d9b", "#FF8769", "#ffc452", "#f9f871"]
sns.set_palette(vivo_c)
g = sns.displot(data=tips, x="total_bill", hue="sex", bins=35, multiple="stack")

g.ax.set_xticks([])
#g.ax.axes.get_yaxis().set_visible(False)
g.ax.set_title("TEST", size=12)
g.ax.patch.set_facecolor('#ffc452')
#sns.despine(right=True)

#g.set(yticks=[])
g.savefig(DIR + '/out/out.png')

