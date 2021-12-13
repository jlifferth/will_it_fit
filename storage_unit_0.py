import matplotlib.pyplot as plt
import numpy as np


# prepare some coordinates
x, y, z = np.indices((10, 10, 10))

# draw cuboids in the top left and bottom right corners, and a link between
# them

# height x width X length
# desk : 2.4 x 4.5 x 2'
# hutch : 7.25 x 5 x 2.16

# code below can be interchanged with notebook
desk = (x < 2) & (y < 5) & (z < 3)
hutch = (x < 3) & (y >= 5) & (z < 8)
tote_1 = (x >= 7) & (y >= 8) & (z < 2)
tote_2 = (x >= 7) & (y < 2) & (z < 2)

# combine the objects into a single boolean array
voxelarray = desk | hutch | tote_1 | tote_2

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[desk] = 'blue'
colors[hutch] = 'green'
colors[tote_1] = 'yellow'
colors[tote_2] = 'pink'


# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
