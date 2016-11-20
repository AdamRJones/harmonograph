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

def posn (time,amplitude,frequency,phase,decay):
    return amplitude* \
           m.sin(time*frequency+phase)* \
           m.e**(-decay*time)

## turtle basics
##
## make turtle go fast by turning off tracing
##graph.tracer(0,0)
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

### x pendulum
##a1=200
###f1=3.12
##p1=0
##d1=.004
##
### y pendulum
##a2=200
###f2=3
##p2=m.pi/2
##d2=.004
##
### gx - gimbal x
##a3=200
###f3=3
##p3=0
##d3=.004
##
### gy- gimbal y
##a4=200
###f4=3.13
##p4=3*m.pi/2
##d4=.004

# x pendulum
a1=200
f1=3.1
p1=0
d1=.04

# y pendulum
a2=200
f2=3
p2=m.pi/3
d2=.04

# gx - gimbal x
a3=0
f3=3
p3=0
d3=.004

# gy- gimbal y
a4=0
f4=3.1
p4=3*m.pi/2
d4=.004

# time and delta
dt=.01
t=0
steps=20000

graph.tracer(0,0)

graph.penup()
x0=posn(0,a1,f1,p1,d1)+posn(0,a3,f3,p3,d3)
y0=posn(0,a2,f2,p2,d2)+posn(0,a4,f4,p4,d4)
graph.setpos(x0,y0)
graph.pendown()

for i in range(1,steps):
    t=t+dt
    x=posn(t,a1,f1,p1,d1)+posn(t,a3,f3,p3,d3)
    y=posn(t,a2,f2,p2,d2)+posn(t,a4,f4,p4,d4)
    graph.setpos(x,y)
graph.update()


