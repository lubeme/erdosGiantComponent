import sys
import netGen

iters = 1000
edgesToGiantComponent={}
p=0.5
n=100
th=float(2)/3
for k in xrange (0, iters):
    giant,numEdges= netGen.bar_ub_zuf(n, p, th)
    if not giant:
        numEdges=0
    if numEdges not in edgesToGiantComponent:
        edgesToGiantComponent[numEdges]=0
    edgesToGiantComponent[numEdges]+=1
print edgesToGiantComponent



