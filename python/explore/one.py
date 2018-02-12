import numpy as np
import numpy as np
import ROOT
import root_numpy
from root_numpy import tree2array, root2array
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cmx


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


filenames = '/home/srq2/Datasets/one_hgcal/ntuple_merged_812.root'
A = root_numpy.root2array(filenames, treename="deepntuplizer/tree", branches=["rechit_energy","rechit_x","rechit_y","rechit_z","rechit_time"])

for i in range(500):
    x = A['rechit_x'][i]
    y = A['rechit_y'][i]
    z = A['rechit_z'][i]
    energy = np.log(A['rechit_energy'][i]+1)


    if len(x) < 10 or len(y) < 10 or len(z) < 10:
        continue

    scatter3d(z,x,y,energy)