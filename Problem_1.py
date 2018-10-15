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

###############################################################################
#Parts a and b
uy = 0
sy = 1.0
true_mean = np.exp(uy+sy/2)
true_median = np.exp(uy)
nonparmeanbias = []
nonparmeanvar = []
nonparmeanMSE = []
nonparmedianbias = []
nonparmedianvar = []
nonparmedianMSE = []
parmeanbias = []
parmeanMSE = []
parmedianbias = []
parmeanvar = []
parmedianvar = []
parmedianMSE = []
X1mean = []
X2mean = []
X1med = []
X2med = []
meanmatrix = []
dfmean = pd.DataFrame
medianmatrix = []
dfmedian = pd.DataFrame
#Sample sizes of 25
for i in range(100000):
    X = np.random.lognormal(uy,sy,25)
    X1 = np.mean(X)#estimate of mean
    X1mean = np.append(X1mean,X1)
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'25' })
    yi = np.log(X)
    ybar = np.mean(yi)
    vy = np.var(yi)
    X2 = np.exp(ybar + vy/2)
    X2mean = np.append(X2mean,X2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'25' })
    b = np.sort(X) #sort to estimate median
    Median1 = b[int((len(b)+1)/2-1)]
    X1med = np.append(X1med,Median1)
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'25' })
    Median2 = np.exp(ybar) #parametric estimate of median
    X2med = np.append(X2med,Median2)
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'25' })
    
a = (np.mean(X1mean)-true_mean)**2
nonparmeanbias = np.append(nonparmeanbias, a)
a = np.var(X1mean)
nonparmeanvar = np.append(nonparmeanvar, a)
a = nonparmeanvar[0] +nonparmeanbias[0]
nonparmeanMSE = np.append(nonparmeanMSE, a)


a = (np.mean(X2mean)-true_mean)**2
parmeanbias = np.append(parmeanbias, a)
a = np.var(X2mean)
parmeanvar = np.append(parmeanvar, a)
a = parmeanvar[0] +parmeanbias[0]
parmeanMSE = np.append(parmeanMSE, a)

a = (np.mean(X1med)-true_median)**2
nonparmedianbias = np.append(nonparmedianbias, a)
a = np.var(X1med)
nonparmedianvar = np.append(nonparmedianvar, a)
a = nonparmedianvar[0] +nonparmedianbias[0]
nonparmedianMSE = np.append(nonparmedianMSE, a)

a = (np.mean(X2med)-true_median)**2
parmedianbias = np.append(parmedianbias, a)
a = np.var(X2med)
parmedianvar = np.append(parmedianvar, a)
a = parmedianvar[0] +parmedianbias[0]
parmedianMSE = np.append(parmedianMSE, a)



X1mean = []
X2mean = []
X1med = []
X2med = []

#Sample sizes of 50
for i in range(100000):
    X = np.random.lognormal(uy,sy,50)
    X1 = np.mean(X) #estimate of mean
    X1mean = np.append(X1mean,X1)
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'50' })
    yi = np.log(X)
    ybar = np.mean(yi)
    vy = np.var(yi)
    X2 = np.exp(ybar + vy/2)
    X2mean = np.append(X2mean,X2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'50' })
    b = np.sort(X) #sort to estimate median
    Median1 = (b[len(b)/2-1]+b[len(b)/2])/2
    X1med = np.append(X1med,Median1)
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'50' })
    Median2 = np.exp(ybar) #parametric estimate of median
    X2med = np.append(X2med,Median2)
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'50' })

a = (np.mean(X1mean)-true_mean)**2
nonparmeanbias = np.append(nonparmeanbias, a)
a = np.var(X1mean)
nonparmeanvar = np.append(nonparmeanvar, a)
a = nonparmeanvar[1] +nonparmeanbias[1]
nonparmeanMSE = np.append(nonparmeanMSE, a)


a = (np.mean(X2mean)-true_mean)**2
parmeanbias = np.append(parmeanbias, a)
a = np.var(X2mean)
parmeanvar = np.append(parmeanvar, a)
a = parmeanvar[1] +parmeanbias[1]
parmeanMSE = np.append(parmeanMSE, a)

a = (np.mean(X1med)-true_median)**2
nonparmedianbias = np.append(nonparmedianbias, a)
a = np.var(X1med)
nonparmedianvar = np.append(nonparmedianvar, a)
a = nonparmedianvar[1] +nonparmedianbias[1]
nonparmedianMSE = np.append(nonparmedianMSE, a)

a = (np.mean(X2med)-true_median)**2
parmedianbias = np.append(parmedianbias, a)
a = np.var(X2med)
parmedianvar = np.append(parmedianvar, a)
a = parmedianvar[1] +parmedianbias[1]
parmedianMSE = np.append(parmedianMSE, a)



X1mean = []
X2mean = []
X1med = []
X2med = []
 
 

#Sample sizes of 100
for i in range(100000):
    X = np.random.lognormal(uy,sy,100)
    X1 = np.mean(X) #estimate of mean
    X1mean = np.append(X1mean,X1)
    meanmatrix.append({'mean': X1, 'P_non_P': 'Non Parametric', 'sample_size':'100' })
    yi = np.log(X)
    ybar = np.mean(yi)
    vy = np.var(yi)
    X2 = np.exp(ybar + vy/2)
    X2mean = np.append(X2mean,X2)
    meanmatrix.append({'mean': X2, 'P_non_P': 'Parametric', 'sample_size':'100' })
    b = np.sort(X) #sort to estimate median
    Median1 = (b[len(b)/2-1]+b[len(b)/2])/2
    X1med = np.append(X1med,Median1)
    medianmatrix.append({'median': Median1, 'P_non_P': 'Non Parametric', 'sample_size':'100' })
    Median2 = np.exp(ybar) #parametric estimate of median
    X2med = np.append(X2med,Median2)
    medianmatrix.append({'median': Median2, 'P_non_P': 'Parametric', 'sample_size':'100' })

a = (np.mean(X1mean)-true_mean)**2
nonparmeanbias = np.append(nonparmeanbias, a)
a = np.var(X1mean)
nonparmeanvar = np.append(nonparmeanvar, a)
a = nonparmeanvar[2] +nonparmeanbias[2]
nonparmeanMSE = np.append(nonparmeanMSE, a)


a = (np.mean(X2mean)-true_mean)**2
parmeanbias = np.append(parmeanbias, a)
a = np.var(X2mean)
parmeanvar = np.append(parmeanvar, a)
a = parmeanvar[2] +parmeanbias[2]
parmeanMSE = np.append(parmeanMSE, a)

a = (np.mean(X1med)-true_median)**2
nonparmedianbias = np.append(nonparmedianbias, a)
a = np.var(X1med)
nonparmedianvar = np.append(nonparmedianvar, a)
a = nonparmedianvar[2] +nonparmedianbias[2]
nonparmedianMSE = np.append(nonparmedianMSE, a)

a = (np.mean(X2med)-true_median)**2
parmedianbias = np.append(parmedianbias, a)
a = np.var(X2med)
parmedianvar = np.append(parmedianvar, a)
a = parmedianvar[2] +parmedianbias[2]
parmedianMSE = np.append(parmedianMSE, a)



X1mean = []
X2mean = []
X1med = []
X2med = []

    
dfmean = pd.DataFrame(meanmatrix)    
dfmedian = pd.DataFrame(medianmatrix)

plt.figure()
ax = sb.boxplot(x = "sample_size", y = "mean", hue = "P_non_P", data=dfmean, palette = "Set3", order = ["25", "50", "100"])
plt.title('Mean')
plt.savefig('mean_boxplot.pdf')  
plt.figure()
ax2 = sb.boxplot(x = "sample_size", y = "median", hue = "P_non_P", data=dfmedian, palette = "Set3", order = ["25", "50", "100"])
plt.title('Median')
plt.savefig('median_boxplot.pdf')  

plt.plot(XX, nonparmeanbias, color = 'r', linestyle = '--')
plt.show()
###############################################################################
#Part c