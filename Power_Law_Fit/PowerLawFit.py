import numpy as np
import pandas as pd
import pylab as plt
from scipy.optimize import curve_fit

def powerlawfn(S,K,gamma):
    '''
    This function returns either Integral source count N(>S) or differential source count n(S)=dN/dS depending on from where you got K and gamma.
    Input parameters:
        S input flux in Jy
        K,gamma : from power law function
    '''
    N=K*(S**(-gamma))
    return N
    


def  diff_powerlaw_fit(Sflux,num_bins,fluxtype=0,method='trf'):
    
    '''
    This function fits power law fit n(S)=KS^(-gamma) from differential source counts.
    
    Input parameters:
        
    Sflux: Input flux in mJy or Jy
    num_bins: Number of bins 
    fluxtype: 0 for mJy and 1 for Jy , default mJy
    method : curve_fit method {'trf','dogbox'}, default is trf

    Return values : ((K,gamma),(standard deviation K,standard deviation gamma))
    '''
    #if fluxtype in mJy then convert to Jy
    if fluxtype==0 :
        Sflux=Sflux/1000. #convert mJy into Jy
    
    
       
    yhist, binedges = np.histogram(Sflux,bins=num_bins)

    bincenters = np.mean(np.vstack([binedges[0:-1],binedges[1:]]), axis=0)
 
    popt,pcov=curve_fit(powerlawfn,bincenters, yhist,method=method,bounds=([0,0], [np.inf, np.inf])) 
    std=np.diag(pcov)**0.5
    
    return popt,std

    
def  int_powerlaw_fit(Sflux,num_bins,fluxtype=0,method='trf'):
    
    '''
    This function fits power law fit N(>S)=CS^(-alpha) from integral source counts.
    
    Input parameters:
        
    Sflux: Input flux in mJy or Jy
    num_bins: Number of bins 
    fluxtype: 0 for mJy and 1 for Jy , default mJy
    method : curve_fit method {'trf','dogbox'}, default is trf
    Return values : ((C,alpha),(standard deviation C,standard deviation alpha))
    '''
    #if fluxtype in mJy then convert to Jy
    if fluxtype==0 :
        Sflux=Sflux/1000. #convert mJy into Jy
    
    
    #print(Sflux)
    yhist, binedges = np.histogram(Sflux,bins=num_bins)
    cumhist=yhist[::-1].cumsum()[::-1]
    


 
    popt,pcov=curve_fit(powerlawfn,binedges[:-1], cumhist,method=method,bounds=([0,0], [np.inf, np.inf])) 
    std=np.diag(pcov)**0.5
    
    return popt,std

    
