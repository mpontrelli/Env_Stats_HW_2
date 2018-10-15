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

meanmatrix = []
dfmean = pd.DataFrame
medianmatrix = []
dfmedian = pd.DataFrame
#O = np.zeros((100000,12))
#Sample sizes of 25
for i in range(100000):
    X = np.random.lognormal(0,1,25)
    X1 = np.sum(X)/len(X) #estimate of mean
    #O[i, 0] = X1
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'25' })
    
    yi = np.log(X)
    ybar = sum(yi) / len(yi)
    vy = sum((yi-ybar)**2)/len(yi)
    X2 = np.exp(ybar + vy/2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'25' })
    #O[i, 1] = X2
    b = np.sort(X) #sort to estimate median
    Median1 = b[int((len(b)+1)/2-1)]
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'25' })
    Median2 = np.exp(ybar) #parametric estimate of median
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'25' })

#Sample sizes of 50
for i in range(100000):
    X = np.random.lognormal(0,1,50)
    X1 = np.sum(X)/len(X) #estimate of mean
    #O[i, 0] = X1
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'50' })
    
    yi = np.log(X)
    ybar = sum(yi) / len(yi)
    vy = sum((yi-ybar)**2)/len(yi)
    X2 = np.exp(ybar + vy/2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'50' })
    #O[i, 1] = X2
    b = np.sort(X) #sort to estimate median
    Median1 = (b[len(b)/2-1]+b[len(b)/2])/2
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'50' })
    Median2 = np.exp(ybar) #parametric estimate of median
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'50' })
        
 

#Sample sizes of 100
for i in range(100000):
    X = np.random.lognormal(0,1,100)
    X1 = np.sum(X)/len(X) #estimate of mean
    #O[i, 0] = X1
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'100' })
    
    yi = np.log(X)
    ybar = sum(yi) / len(yi)
    vy = sum((yi-ybar)**2)/len(yi)
    X2 = np.exp(ybar + vy/2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'100' })
    #O[i, 1] = X2
    b = np.sort(X) #sort to estimate median
    Median1 = (b[len(b)/2-1]+b[len(b)/2])/2
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'100' })
    Median2 = np.exp(ybar) #parametric estimate of median
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'100' })
       
dfmean = pd.DataFrame(meanmatrix)    
dfmedian = pd.DataFrame(medianmatrix)

plt.figure()
ax = sb.boxplot(x = "sample_size", y = "mean", hue = "P_non_P", data=dfmean, palette = "Set3", order = ["25", "50", "100"])
plt.figure()
ax2 = sb.boxplot(x = "sample_size", y = "median", hue = "P_non_P", data=dfmedian, palette = "Set3", order = ["25", "50", "100"])