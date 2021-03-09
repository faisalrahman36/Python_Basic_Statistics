#Variance and Standard Deviation
import numpy as np
y=[2.1,4.1,6.1,8.1,10.1,12.1,14.1,16.1,18.1,20.1]
x=[1,2,3,4,5,6,7,8,9,10]

meanx=np.mean(x)
meany=np.mean(y)

#for x
nx=len(x) 
vx=np.linspace(0,1,num=len(x))

for i in range(0,len(x)):
    vx[i]=(x[i]-meanx)**2
pvarx=np.sum(vx)/(nx) #population variance
svarx=np.sum(vx)/(nx-1) #sample variance
psdx=np.sqrt(pvarx)  #population standard deviations
ssdx=np.sqrt(svarx)  #sample standard deviations
#for y
ny=len(y) 
vy=np.linspace(0,1,num=len(y))

for i in range(0,len(y)):
    vy[i]=(y[i]-meany)**2
pvary=np.sum(vy)/(ny) #population variance
svary=np.sum(vy)/(ny-1) #sample variance
psdy=np.sqrt(pvary)  #population standard deviations
ssdy=np.sqrt(svary)  #sample standard deviations


print(meanx)
print(meany)
print(pvarx)
print(pvary)
print(svarx)
print(svary)

print(psdx)
print(psdy)
print(ssdx)
print(ssdy)

