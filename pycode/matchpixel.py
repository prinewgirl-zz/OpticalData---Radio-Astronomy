#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:25:01 2020

@author: priscila
"""
from astropy.coordinates import SkyCoord
from astropy.coordinates import match_coordinates_sky
from astropy.table import Table
import os
import sys
  
gama = Table.read(sys.argv[1])
path_dir = sys.argv[2]
path_new = sys.argv[3]
error = float(sys.argv[4])

def matching_index(base_catalog_ra, base_catalog_dec, catalog_ra, catalog_dec,
                   error):
   
    c = SkyCoord(ra=base_catalog_ra, dec=base_catalog_dec, unit="deg")
    catalog = SkyCoord(ra=catalog_ra, dec=catalog_dec, unit="deg")
    idx, d2d, d3d = match_coordinates_sky(c, catalog)
    idx = idx[d2d.arcsec < error] #error in arcsecs
    return idx

for i,filename in enumerate(os.listdir(path_dir)):
    file_ = Table.read(os.path.join(path_dir,filename))
    index = matching_index(gama['RA'],gama['DEC'], file_['RA'],
                           file_['DEC'], error)
    #test if the list is not empty
#   #print(index)
    if len(index) != 0:
        table = Table(names = file_.colnames)
        for j in index:
            table.add_row(file_[j])
            #print("one line written")
        table.write(os.path.join(path_new,filename))
