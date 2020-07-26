#main file

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from Dreamer import Dream, DreamExtractor

dream_loader = DreamExtractor(dream_file='./dreams/badea/Badea2011Brn3aONandOFF-RCNG.swc')

dream_loader.read_dream()
generated_dream = dream_loader.generate_dream()

new_dream = Dream( generated_dream.dreamtree, generated_dream.raw_point_data )

fig = plt.figure()

data = np.dstack(new_dream.raw_point_data)
data = data[0, ...]
print(data.shape)

ax = fig.add_subplot( 111 , projection='3d')
ax.scatter(data[0, :], data[1, :], data[2, :], c='r', marker='o')
plt.show() 