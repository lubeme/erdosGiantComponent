from pylab import *
import numpy as np
from scipy.stats import gaussian_kde
import netGen
from scipy.interpolate import UnivariateSpline

iters = 100
edgesToGiantComponent={}
p=0.1
n=100
th=float(2)/3
for k in xrange (0, iters):
    if k>0 and k%(iters/10)==0:
        print "iteracion:",k
    giant,numEdges= netGen.bar_ub_zuf(n, p, th)
    if not giant:
        numEdges=0
    if numEdges not in edgesToGiantComponent:
        edgesToGiantComponent[numEdges]=0
    edgesToGiantComponent[numEdges]+=1

x=xrange(0,n*(n-1)/2+1)
y=[0]*(n*(n-1)/2+1)
for element in edgesToGiantComponent:
    y[element]=edgesToGiantComponent[element]/float(iters)
 
Ycdf=np.cumsum(y)

plot(x,y,'bo',label="pdf")
plot(x,Ycdf,'r--',label="cdf")
xlim(0,len(x))
ylim(0,1.1)
legend(loc='upper-left')

show()

