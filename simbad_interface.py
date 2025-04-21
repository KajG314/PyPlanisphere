# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:25:42 2022

@author: Kaj
"""

import astropy
import numpy as np
from astroquery.simbad import Simbad

Simbad.TIMEOUT = 120
#Simbad.list_votable_fields()

Simbad.add_votable_fields("ra", "dec", 'typed_id', 'flux(V)', 'plx')
Simbad.remove_votable_fields("coordinates", "diameter")
print(Simbad.get_votable_fields())


"""
want (in no particular order):
    
    diameter
    ra
    dec
    flux(V)
    parallax
    typed ids

"""


#result = Simbad.query_criteria("otype=* & Vmag<6")
#print(result)

   
#result.write('star_names.csv', format='ascii', overwrite=True)


raw_star_data = np.loadtxt('star_names.csv', dtype=str, delimiter=',')
#print(np.shape(star_data))

print(raw_star_data[0])
split_first_star_row = raw_star_data[1].split("\" ")

first_star_row = []

for x in split_first_star_row:
    x = x.replace("\"", "")
    first_star_row.append(x)
    
print(first_star_row)