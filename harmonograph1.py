#-------------------------------------------------------------------------------
# Name:        harmonograph
# Purpose:
#
# Author:      Adam & Matthew
#
# Created:     12/11/2016
# Copyright:   (c) Adam & Matthew 2016
#-------------------------------------------------------------------------------


import turtle as graph
import math as m


##
## make turtle go fast
##t.tracer(0,0)
##
##for x in range(500):
##    t.forward (x)
##    t.right (170)
##
## only needed if turtle.tracer(0,0) used earlier
##t.update()


###period and frequency
##
### g is acceleration due to gravity = 9.8m/s^2
##g = 9.8
##
##for i in range(1,10):
##    length = i/10
##    # compute period
##    p = 2 * m.pi * m.sqrt(length/g)
##    # computer frequency
##    f = 1/p
##    print (length,p,f)


# harmonograph
A1=56
F1=5
P1=0
D1=.2

A2=73
F2=5
P2=m.pi/4
D2=.2

dt=.01
t=0

for i in range(1,1000):
    t=t+dt
    x=A1*m.sin(t*F1+P1)*m.e**(-D1*t)
    y=A2*m.sin(t*F2+P2)*m.e**(-D2*t)
    graph.setpos(x,y)
