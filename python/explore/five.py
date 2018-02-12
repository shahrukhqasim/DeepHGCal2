from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cmx
from visualize.basic_visualizer import BasicVisualizer
from explore.grab_interesting_points import GrabMaximumPoints

def scatter3d(x,y,z, cs, colorsMap='Reds'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(np.exp(cs)), s=np.log(cs+1)*100)
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()



with open('/home/srq2/Datasets/one_hgcal/input/input.npy') as f:
    X = np.load(f)
    print("File read!")

X = X[0]

#scatter3d(x,y,z,energy)

visualizer = BasicVisualizer(GrabMaximumPoints())
visualizer.add_layer(X)
visualizer.add_layer(X + 30)
visualizer.show()