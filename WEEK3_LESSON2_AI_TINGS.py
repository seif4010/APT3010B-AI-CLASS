import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import random

# creating a line graph
varX = random.randint(100, size=(100))
varY = random.randint(100, size=(100))

varX.sort()
varY.sort()
# plotting the graph
plt.plot(varX, varY)
# display the graph
plt.show()

# histogram
varZ = random.normal(170, 10, 250)
plt.hist(varZ)
plt.show()

# csv file to be manipulated visualization
scores = pd.read_csv("pokemon.csv")


def ThouBoxPlot():
    sns.boxplot(data=scores)
    plt.show()


def MyScatterPlot():
    sns.lmplot(x="Attack", y="Defense", data=scores,
               fit_reg=False, hue="Speed")
    plt.show()


def MyLinePlot():
    sns.lineplot(x="Attack", y="Defense", data=scores)
    plt.show()


ThouBoxPlot()
MyLinePlot()
MyScatterPlot()
