import pandas as pd
import matplotlib.pyplot as plt

graph = pd.read_csv('train.csv', index_col=0)
plot = graph.plot('Something', lw=2, colormap='jet', mnarker='.', markersize=10)
plot.set_xlabel("who")
plot.set_ylabel("how")
plt.savefig('test.png')