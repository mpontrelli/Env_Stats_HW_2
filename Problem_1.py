# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:21:28 2018

@author: mpontr01
"""

import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

O = np.zeros((100000, 12))

#Sample sizes of 25
for i in range(100000):
    X = np.random.lognormal(0,1,26)
    O[i,0] = np.sum(X)/len(X) #estimate of mean
    
    
    b = np.sort(X) #sort to estimate median
    if len(X) % 2 == 0:
        O[i:2] = (b[len(b)/2-1]+b[len(b)/2])/2
    else:
        O[i:2] = b[(len(b)+1)/2-1]
            
        
    
    

#Testing github
# another test

#df3 = pd.DataFrame(O,columns=['25X1', '25X2', '25x0.51', '25x0.52',
           #        '50X1', '50X2', '50x0.51', '50x0.52',
           #        '100X1', '100X2', '100x0.51', '100x0.52',])

# Direct generation


#I don't know the right way to code this...
#U = np.random.normal(0,1,100000)
#X = np.exp(U)
#plt.figure()
#sb.distplot(X,hist = True)
