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


## turtle basics
##
## make turtle go fast by turning off tracing
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

### sin function
###
##steps = 1000
##dx = .1
##x=0
##amplitude = 100
##for i in range (0,steps):
##    x = x + dx
##    y = amplitude*m.sin(x)
##    #print (x,y)
##    graph.setpos (x*10,y)

# harmonograph

# pendulum formula: amplitude *
#                   sin(time*frequency + phase_offset) *
#                   e**(-time*damping_constant)

# x pendulum
a1=300
f1=5
p1=0
d1=.2

# y pendulum
a2=350
f2=5
p2=m.pi/4
d2=.2

# time and delta
dt=.01
t=0

for i in range(1,2000):
    t=t+dt
    x=a1*m.sin(t*f1+p1)*m.e**(-d1*t)
    y=a1*m.sin(t*f2+p2)*m.e**(-d2*t)
    graph.setpos(x,y)
