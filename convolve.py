
from math import *


def convolve_old(xdat,ydat,sigma,scale=1.):
  print "running convolve() with sigma: ",sigma
  dx=xdat[1]-xdat[0]      # assume fixed spacing
  out=[0. for i in range(len(xdat))]
  for i in range(len(xdat)):
    if sigma[i] == 0.: out[i]=ydat[i]   # no convolution necessary

    xp=[(x-xdat[i])/sigma[i] for x in xdat]
    asum=0.
    bsum=0.

    # first point has factor of 1/2
    dint=0.5*exp(-0.5*xp[0]*xp[0])
    asum+=ydat[0]*dint
    bsum+=dint

    # middle points
    for j in range(1,len(xdat)-1):
      dint=exp(-0.5*xp[j]*xp[j])
      asum+=ydat[j]*dint
      bsum+=dint

    # last point has factor of 1/2
    dint=0.5*exp(-0.5*xp[-1]*xp[-1])
    asum+=ydat[-1]*dint
    bsum+=dint

    out[i]=scale*asum/bsum

  return out
