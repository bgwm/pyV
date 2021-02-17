import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots()

# Load the example car crash dataset
tips = sns.load_dataset("tips")

# Plot the total crashes
#sns.set_color_codes("pastel")
#sns.barplot(x="tip", y="sex", data=tips, label="Total", color="b")

# Plot the crashes where alcohol was involved
#sns.set_color_codes("muted")
#sns.barplot(x="size", y="sex", data=crashes,
#            label="Alcohol-involved", color="b")

sns.histplot(data=tips, x="total_bill", hue="sex", bins=35, multiple="stack",
        label="sex")
print("22")
# Add a legend and informative axis label
ax.legend(ncol=2, frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)
plt.show()
f.savefig('x.png')
