#%%
import random
import math
from matplotlib import pyplot as plt
import numpy as np
import csv
from matplotlib.patches import Circle, Rectangle
import julia
import os
import datetime


#%% RUN OUR LOCAL VERSION OF LUBACHEVSKY
#os.system("rm -f ./LS/spheres.exe")
os.system("rm -f ./LS/spheres")
os.chdir("LS")
os.system("ls")
os.system("make")
os.system("./spheres input.txt")

#%% CONVERT LS TO 106 MM DOMAIN
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


filename = os.getcwd() + "/write.dat"
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


indices_rem = []
for i in range(len(pts)):
    if distance((pts[i][0], pts[i][1]), (53, 53)) > (53-1):
        indices_rem.append(i)
    
    #if distance((pts[i][0], pts[i][1]), (53, 53)) < 5.5:
    #    indices_rem.append(i)
indices_rem.sort()
indices_rem = set(indices_rem)


print(len(pts))
pts = [v for i, v in enumerate(pts) if i not in indices_rem]
print(len(pts))

file = open("input_Calippso.dat", 'w')
file.write("2\n")
file.write("2969\n")
file.write(f"{multiplier}\n")
for i in range(len(xs)):
    file.write(str(xs[i]) + " " + str(ys[i]) + "\n")

file.close()
fig,ax = plt.subplots(1)
ax.set_aspect('equal')

r = 1
lowerbound = -2
upperbound = 108

fig.set_size_inches(12, 12)
ax.set(xlim=(lowerbound, upperbound), ylim=(lowerbound, upperbound))


for i in range(0, len(pts)):
    circ = Circle((pts[i][0], pts[i][1]), r, fill=True, color = 'k')
    ax.add_patch(circ)   

big_circ = Circle((53, 53), 53, fill=False, color='r')
ax.add_patch(big_circ)

checkpoint = datetime.datetime.now()

fig.savefig(f'datums/before_calippso{checkpoint}.png')

#%%RUN CALIPPSO
j = julia.Julia(compiled_modules=False)
ran = j.include("calippso.jl")

# %% make final image
lines = open("output_Calippso.txt").read().splitlines()
pts = []
xs = []
ys = []

for line in lines:
    temp = line.split(", ")
    pts.append((float(temp[0]) , float(temp[1]) ))

for pt in pts:
    xs.append(pt[0])
    ys.append(pt[1])


indices_rem = []
for i in range(len(pts)):
    if distance((pts[i][0], pts[i][1]), (53, 53)) > (53-1):
        indices_rem.append(i)
    
    if distance((pts[i][0], pts[i][1]), (53, 53)) < 5.5:
        indices_rem.append(i)
indices_rem.sort()
indices_rem = set(indices_rem)


print(len(pts))
pts = [v for i, v in enumerate(pts) if i not in indices_rem]
print(len(pts))

fig,ax = plt.subplots(1)
ax.set_aspect('equal')

r = 1
lowerbound = -2
upperbound = 108

fig.set_size_inches(12, 12)
ax.set(xlim=(lowerbound, upperbound), ylim=(lowerbound, upperbound))

for i in range(0, len(pts)):
    circ = Circle((pts[i][0], pts[i][1]), r, fill=True, color = 'k')
    ax.add_patch(circ)   

big_circ = Circle((53, 53), 53, fill=False, color='r')
ax.add_patch(big_circ)


fig.savefig(f'datums/after_calippso{checkpoint}.png')
# %%
