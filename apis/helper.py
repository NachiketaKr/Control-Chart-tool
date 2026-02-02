import numpy as np
import pandas as pd
from scipy import stats

def test_near(X,limits,data_point,which_limit):
    count = 0 
    s = len(limits)
    a=0
    b=1
    if(which_limit=="UCL"):
        a=s-2
        b=s-1
    if(data_point>=limits[a] and data_point<=limits[b]):
        count = count+1 
    else:
        return 0
    for j in range(0,2):
        if(X[j]>=limits[a] and X[j]<=limits[b]):
            count+= 1
    if(count >= 2):
        return 1
    else:
        return 0

def test_bUC_bLC(X,limits,data_point,type_of_test):
    a=1
    b=2
    if(type_of_test=="bUC"):
        a=4
        b=5        
    count = 0 
    if(data_point>=limits[a] and data_point<=limits[b]):
        count = count+1 
    else:
        return 0
    for j in range(0,4):
        if(X[j]>=limits[a] and X[j]<=limits[b]):
            count+= 1
    if(count >= 4):
        return 1
    else:
        return 0


def test_trend_ud(X,limits,data_point):
    s = len(limits)
    c = 0
    if(s == 7):
        c = 3
    else:
        c = 2
    count = 0
    
    a=c+1
    b=c-1
    if(data_point <= limits[a] and data_point >= limits[b]):
        count +=1
    else:
        return 0 
    for j in range(0,6):
        if(X[j]<=limits[a]and X[j]>=limits[b]):
            count+= 1
    if(count >= 7):
        return 1
    else:
        return 0
    
#----------------------------Check data for linear trend-----------------------#
def linearity(data):
    Y=np.zeros(len(data))
    x= np.zeros(len(data))
    for i in range(0,len(data)):
        Y[i]= i
        x[i]= data[i]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,Y)
    if(r_value**2>0.33 and p_value<0.01):
        return 0
    else:
        return 1

#----------------------------Check data for normality--------------------------#
def normality(X):
    data = np.zeros(len(X))
    mean = np.mean(X)
    std_dev = np.std(X,ddof = 1)
    for i in range(0, len(X)):
        data[i] = (X[i]-mean)/std_dev
    x = stats.kstest(data, 'norm')
    if(x.pvalue < 0.05):
        return 0
    else:
        return 1 

#----------------Generates control limits for a particular data----------------#
def limits_generator(data, coef):
    mean = np.mean(data)
    std_dev = np.std(data,ddof = 1)
    if(coef == 3):
        limits = []
        for i in range(0,7):
            limits.append(mean-3*std_dev+i*std_dev)
        return limits
    elif(coef == 2):
        limits = []
        for i in range(0,5):
            limits.append(mean-2*std_dev+i*std_dev)

    return limits

#----------------Generates control limits for a given specification limit----------------#
def specification_limits_generator(lcl,ucl,coef):
    std_dev=(ucl-lcl)/6
    mean=(lcl+ucl)/2
    if(coef == 3):
        limits = []
        for i in range(0,7):
            limits.append(mean-3*std_dev+i*std_dev)
        return limits
    elif(coef == 2):
        limits = []
        for i in range(0,5):
            limits.append(mean-2*std_dev+i*std_dev)
    
    return limits
