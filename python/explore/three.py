from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cmx
from visualize.basic_visualizer import BasicVisualizer
from explore.grab_interesting_points import GrabInterestPointsInterface

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
X = np.sum(X, axis=3)

I = np.argwhere(X>0)

l,s = np.shape(I)

energy=[]
for i in range(l):
    index = tuple(I[i].tolist())
    print("Value",X[index], "Index", index)
    energy.append(float(X[index]))

print("Total", l, "non-zero places")


x = I[:,0]
y = I[:,1]
z = I[:,2]

print(len(energy),len(x),len(y),len(z))

x = np.array(x)
y = np.array(y)
z = np.array(z)
energy = np.array(energy)

D = np.concatenate((np.expand_dims(x,0),np.expand_dims(y,0),np.expand_dims(z,0),np.expand_dims(energy,0)))

#scatter3d(x,y,z,energy)

visualizer = BasicVisualizer(GrabInterestPointsInterface())
visualizer.add_layer(D)
visualizer.add_layer(D + 30)
visualizer.show()