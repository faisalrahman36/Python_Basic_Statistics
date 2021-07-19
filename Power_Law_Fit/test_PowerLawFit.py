import PowerLawFit as plf
import numpy as np
import matplotlib.pyplot as plt

#Test for PowerLawFit.py

#random data as input using power law P(x)=ax^(a-1) with 0<x<1 and a>0 with 
a = .5 
number_bins = 20000  #Number of flux bins or basically bin centers for catalog sources.
s_flux = np.random.power(a, number_bins)   
true_model=a*s_flux**(a-1) #sample sources per bin or differential source count per bin

'''
a=0.5 will give an input data model of (not exactly but good approximation):
true_model=0.5*s_flux**(-0.5)

Our differential count fit model should recover something closed to this.

'''
#print(s_flux)
#print(min(s_flux),max(s_flux))
params,std=plf.int_powerlaw_fit(s_flux,num_bins=number_bins,fluxtype=1,method='trf')


C=params[0]
alpha=params[1]
stdC=std[0]
stdalpha=std[1]
print('C ',C,' alpha ',alpha,' std C ',stdC,' std alpha ',stdalpha)

params,std=plf.diff_powerlaw_fit(s_flux,num_bins=number_bins,fluxtype=1,method='trf')
K=params[0]
gamma=params[1]
stdK=std[0]
stdgamma=std[1]
print('K ',K,' gamma ',gamma,' std K ',stdK,' std gamma ',stdgamma)

fit_model=K*s_flux**(-gamma) #for comparison with true model
plt.plot(s_flux,fit_model,'bs',label='fit model')
plt.plot(s_flux,true_model,'r+',label='true model')
plt.title('Differential power law fit test')
#plt.xscale('log')
plt.yscale('log')
plt.xlabel('S')
plt.ylabel('n(s)')
plt.show()
