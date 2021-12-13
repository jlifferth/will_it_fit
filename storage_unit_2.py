import matplotlib.pyplot as plt
import numpy as np

# prepare some coordinates
x, y, z = np.indices((10, 10, 10))

desk = (x < 2) & (y < 5) & (z < 3)
hutch = (x < 3) & (y >= 5) & (z < 8)
tote_6 = (x >= 3) & (x < 5) & (y >= 7) & (y < 10) & (z >= 0) & (z < 2)
tote_7 = (x >= 3) & (x < 5) & (y >= 7) & (y < 10) & (z >= 2) & (z < 4)
tote_8 = (x >= 3) & (x < 5) & (y >= 7) & (y < 10) & (z >= 4) & (z < 6)
tote_9 = (x >= 3) & (x < 5) & (y >= 7) & (y < 10) & (z >= 6) & (z < 8)
tote_10 = (x >= 3) & (x < 5) & (y >= 4) & (y < 7) & (z >= 0) & (z < 2)
tote_11 = (x >= 3) & (x < 5) & (y >= 4) & (y < 7) & (z >= 2) & (z < 4)
tote_12 = (x >= 3) & (x < 5) & (y >= 4) & (y < 7) & (z >= 4) & (z < 6)
tote_13 = (x >= 3) & (x < 5) & (y >= 4) & (y < 7) & (z >= 6) & (z < 8)
toaster = (x >= 3) & (x < 5) & (y >= 3) & (y < 4) & (z >= 0) & (z < 1)
bike = (x >= 2) & (x < 3) & (y >= 0) & (y < 5) & (z >= 0) & (z < 5)
chest = (x >= 0) & (x < 2) & (y >= 2) & (y < 5) & (z >= 3) & (z < 5)

# combine the objects into a single boolean array
voxelarray = desk | hutch | tote_6 | tote_7 | tote_8 | tote_9 | tote_10 | tote_11 | tote_12 | tote_13 | toaster | bike | chest

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[desk] = 'blue'
colors[hutch] = 'green'
colors[tote_6] = 'black'
colors[tote_7] = 'yellow'
colors[tote_8] = 'black'
colors[tote_9] = 'yellow'
colors[tote_10] = 'yellow'
colors[tote_11] = 'black'
colors[tote_12] = 'yellow'
colors[tote_13] = 'black'
colors[toaster] = 'silver'
colors[bike] = 'cyan'
colors[chest] = 'red'

# and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')
# plt.rcParams["figure.figsize"] = (5,5)
# plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)


plt.show()
