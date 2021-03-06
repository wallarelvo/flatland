import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.patches as patches
from matplotlib.patches import Circle
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import matplotlib.cm as cm
import os
import pdb


rrtPath = "sandbox/prmpath.txt"
obstacleFolder = 'sandbox/obstacles/'


def generate_codes(length):
    codes = list()
    codes.append(Path.MOVETO)
    for _ in xrange(1, length - 1):
        codes.append(Path.LINETO)
    codes.append(Path.STOP)
    return codes


def make_path_plot_2d():
    fig1 = plt.figure()

    for i in os.listdir(obstacleFolder):
        obstaclePath = obstacleFolder + i

        #ob = np.loadtxt(obstaclePath)
        #ob = np.vstack((ob, ob[0, :]))
        #CH = Delaunay(ob).convex_hull
        #x,y = ob[:,0],ob[:,1]
        #z = np.zeros_like(x)

        #ax = fig1.gca(projection='3d')
        #S = ax.plot_trisurf(x,y,z,triangles=CH,shade=True,cmap=cm.autumn,lw=0.2)

        ob = np.loadtxt(obstaclePath)
        ob = np.vstack((ob, ob[0, :]))
        hull = ConvexHull(ob)
        newHull = []
        for p in hull.vertices:
            newHull.append(ob[p])
        newHull.append(ob[hull.vertices[0]])
        path = Path(newHull)
        patch = patches.PathPatch(path, facecolor='orange', lw=2)
        ax = plt.gca()
        ax.add_patch(patch)


    txt = np.loadtxt(rrtPath)
    start = txt[0,0:2]
    goal = txt[-1,0:2]

    #startCircle = plt.Circle(start,0.3,color='g', zorder=2)
    #goalCircle = plt.Circle(goal,0.3,color='r', zorder=2)
    #fig1.gca().add_artist(startCircle)
    #fig1.gca().add_artist(goalCircle)
    startCircle = Circle(start,1,color='g',zorder=2)
    goalCircle = Circle(goal,1,color='r',zorder=2)
    ax.add_patch(startCircle)
    ax.add_patch(goalCircle)
    #art3d.pathpatch_2d_to_3d(startCircle,z=0,zdir='z')
    #art3d.pathpatch_2d_to_3d(goalCircle,z=0,zdir='z')

    plt.plot(txt[:, 0], txt[:, 1], 'bo-', markersize=10, linewidth=3, zorder=1)

def make_path_plot_3d():
    fig1 = plt.figure()
    ax = fig1.gca(projection='3d')

    for i in os.listdir(obstacleFolder):
        obstaclePath = obstacleFolder + i

        ob = np.loadtxt(obstaclePath)
        ob = np.vstack((ob, ob[0, :]))
        CH = Delaunay(ob).convex_hull
        x,y,z = ob[:,0],ob[:,1],ob[:,2]

        S = ax.plot_trisurf(x,y,z,triangles=CH,shade=True,cmap=cm.copper,lw=0.2)

    txt = np.loadtxt(rrtPath)
    start = txt[0,0:2]
    goal = txt[-1,0:2]

    startCircle = Circle(start,2,color='g')
    goalCircle = Circle(goal,2,color='r')
    ax.add_patch(startCircle)
    ax.add_patch(goalCircle)
    art3d.pathpatch_2d_to_3d(startCircle,z=txt[0,2],zdir='y')
    art3d.pathpatch_2d_to_3d(goalCircle,z=txt[-1,2],zdir='y')

    plt.plot(txt[:, 0], txt[:, 1], txt[:,2], 'bo-', markersize=10, linewidth=3)

if __name__ == "__main__":
    import sys
    if sys.argv[1] == "2":
        make_path_plot_2d()
    else:
        make_path_plot_3d()
    plt.show()
