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
    X = np.random.lognormal(0,1,25)
    X1 = np.sum(X)/len(X) #estimate of mean
    O[i, 0] = X1
    
    
    yi = np.log(X)
    ybar = sum(yi) / len(yi)
    vy = sum((yi-ybar)**2)/len(yi)
    X2 = np.exp(ybar + vy/2)
    O[i, 1] = X2
    
    O[i,3] = np.exp(X1) #parametric estimate of median
    b = np.sort(X) #sort to estimate median
    if len(X) % 2 == 0: #if n is even
        O[i,2] = (b[len(b)/2-1]+b[len(b)/2])//2
    else: #if n is odd
        O[i,2] = b[int((len(b)+1)/2-1)]
        
        
#Sample sizes of 50
for i in range(100000):
    vy = np.array([])
    X = np.random.lognormal(0,1,50)
    X1 = np.sum(X)/len(X) #estimate of mean
    O[i, 4] = X1
    
    for j in range(len(X)):
        q = (np.log(X[j]) - X1)**2
        vy = np.append(vy, q)
    z = sum(vy)/len(X)
    X2 = np.exp(X1 + z/2)
    O[i, 5] = X2
    
    O[i,7] = np.exp(X1) #parametric estimate of median
    b = np.sort(X) #sort to estimate median
    if len(X) % 2 == 0: #if n is even
        O[i,6] = (b[len(b)//2-1]+b[len(b)//2])//2
    else: #if n is odd
        O[i,6] = b[(len(b)+1)//2-1]
        
        
        
#Sample sizes of 100
for i in range(100000):
    vy = np.array([])
    X = np.random.lognormal(0,1,100)
    X1 = np.sum(X)/len(X) #estimate of mean
    O[i, 8] = X1
    for j in range(len(X)):
        q = (np.log(X[j]) - X1)**2
        vy = np.append(vy, q)
    z = sum(vy)/len(X)
    X2 = np.exp(X1 + z/2)
    O[i, 9] = X2
    O[i,11] = np.exp(X1) #parametric estimate of median
    b = np.sort(X) #sort to estimate median
    if len(X) % 2 == 0: #if n is even
        O[i,10] = (b[len(b)//2-1]+b[len(b)//2])//2
    else: #if n is odd
        O[i,10] = b[(len(b)+1)//2-1]
      
        
            
        
    
#    
#
##Testing github
## another test
#
#df3 = pd.DataFrame(O,columns=['25X1', '25X2', '25x0.51', '25x0.52',
#                   '50X1', '50X2', '50x0.51', '50x0.52',
#                   '100X1', '100X2', '100x0.51', '100x0.52',])



# Direct generation


#I don't know the right way to code this...
#U = np.random.normal(0,1,100000)
#X = np.exp(U)
#plt.figure()
#sb.distplot(X,hist = True)
