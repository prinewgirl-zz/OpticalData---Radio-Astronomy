from astropy.table import Table, join, hstack
from esutil import htm
import numpy as np
import random
import sys
import os

def match(cat_1, cat_2, column_1, column_2, column_3, column_4,error):
    h = htm.HTM(depth=10)
    m1, m2, d12 = h.match(np.array(cat_1[column_1]), 
                          np.array(cat_1[column_3]),
                          np.array(cat_2[column_2]), 
                          np.array(cat_2[column_4]),
                          error, maxmatch=1)
    
    submatched = cat_1[m1]
    manmatched = cat_2[m2]
    matched = hstack([submatched, manmatched])
      
    return matched
def add_randomcol(cat):
    """Input: 
    cat: DataFrame
    Output:
    DataFrame with a random column
    """
    cat['random'] = 1.5
    return cat

error = 0.00028
path_new = sys.argv[3] 
gama = Table.read(sys.argv[1])
path_dir = sys.argv[2]

for i,filename in enumerate(os.listdir(path_dir)):
    #print(filename)
    file_ = Table.read(os.path.join(path_dir,filename))
    data = match(gama, file_,'RA','RA','DEC','DEC',error)
    if len(data) != 0:
        data.add_column(1.5, name = 'random')
        for i in range(0, len(data)):
            data[i]['random'] = np.random.random()
    #if len(data['RA']) != 0:
    filename = 'match_' + filename
    data.write(os.path.join(path_new,filename))
