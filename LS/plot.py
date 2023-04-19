#%%

import random
import math
from matplotlib import pyplot as plt
import numpy as np
import csv
from matplotlib.patches import Circle, Rectangle
import os

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

filename = "C:\\Users\\jo\\Desktop\\dolbow\\LS\\write.dat"
lines = open(filename).read().splitlines()
multiplier = 2 / float(lines[3])
print(lines[3])
print(multiplier)
#coordinates start at index = 6
lines = lines[6:]
pts = []
xs = []
ys = []
for line in lines:
    temp = line.split()
    pts.append((float(temp[0]) * multiplier , float(temp[1]) * multiplier ))

for pt in pts:
    xs.append(pt[0])
    ys.append(pt[1])


all_in = True
indices_rem = []
for i in range(len(pts)):
    if distance((pts[i][0], pts[i][1]), (53, 53)) > (53-1):
        indices_rem.append(i)
    
    if distance((pts[i][0], pts[i][1]), (53, 53)) < 5.5:
        indices_rem.append(i)


file = open("C:\\Users\\jo\\Desktop\\dolbow\\LS\\2969.dat", 'w')
file.write("2\n")
file.write("2969\n")
file.write(f"{multiplier}\n")



indices_rem.sort()
#print(indices_rem)
indices_rem = set(indices_rem)


print(len(pts))
pts = [v for i, v in enumerate(pts) if i not in indices_rem]
print(len(pts))
#print(all_in)


for i in range(len(xs)):
    file.write(str(xs[i]) + " " + str(ys[i]) + "\n")

r = 1
        
fig,ax = plt.subplots(1)
ax.set_aspect('equal')

lowerbound = -2
upperbound = 108

fig.set_size_inches(12, 12)
ax.set(xlim=(lowerbound, upperbound), ylim=(lowerbound, upperbound))
''''''


for i in range(0, len(pts)):
    #if distance([xs[i], ys[i]], [26.5, 26.5]) <= 26.5 and distance([xs[i], ys[i]], [26.5, 26.5]) >= 5:
    circ = Circle((pts[i][0], pts[i][1]), r, fill=True, color = 'k')
    ax.add_patch(circ)   

big_circ = Circle((53, 53), 53, fill=False, color='r')
ax.add_patch(big_circ)

#lil_circ = Circle((53, 53), 5, fill=False, color='r')
#ax.add_patch(lil_circ)


fig.savefig("2969.png")

file.close()
# %%
