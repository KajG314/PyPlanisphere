# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:15:59 2022

@author: Kaj
"""

import numpy as np
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u

x = np.load('gaia_all.npy')
ra = x[:,0]
dec = x[:,1]
px = x[:,2]
pe = x[:,3]
g = x[:,4]
bmr = x[:,5]

#x_csv = np.savetxt("gaia_all.csv", x, delimiter=",")

d = 1/(px/1000)
#M = g - 5 * np.log10(d) + 5


print(px[0])
print(d[0])


vis_ra = []
vis_dec = []

i = 0
for i in range(np.size(x[:, 0])):
    if g[i] <= 6:
        vis_ra.append(x[i, 0])
        vis_dec.append(x[i, 1])
        i += 1
        continue
    else:
        i += 1
        continue

vis_cp_ra = []
vis_cp_dec = []

print(vis_dec[0])

a = 0
for d in vis_dec:
    if d > 41:
        vis_cp_ra.append(x[a, 0])
        vis_cp_dec.append(x[a, 1])
        a += 1
        continue
    else:
        a+=1
        continue
    
    

raa,dca = coord.Angle(ra*u.deg),coord.Angle(dec*u.deg)
raa = raa.wrap_at(180.*u.degree)

vis_raa, vis_dca = coord.Angle(vis_ra*u.deg), coord.Angle(vis_dec*u.deg)
vis_raa = vis_raa.wrap_at(180.*u.degree)

vis_cp_raa, vis_cp_deca = coord.Angle(vis_cp_ra*u.deg), coord.Angle(vis_cp_dec*u.deg)
vis_cp_raa = vis_cp_raa.wrap_at(180*u.degree)

fig = plt.figure(num=1,figsize=(10,5))

ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(raa.radian,dca.radian,s=0.01,marker='.',color='blue')
ax.scatter(vis_raa.radian, vis_dca.radian, s=0.5, marker='x', color='red')
ax.scatter(vis_cp_raa.radian, vis_cp_deca.radian, s=0.75, marker='o', color='forestgreen')