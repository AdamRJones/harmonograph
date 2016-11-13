#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adam & Matthew
#
# Created:     12/11/2016
# Copyright:   (c) Adam & Matthew 2016
#-------------------------------------------------------------------------------


import turtle as graph
import math as m


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
##
##steps = 1000
##dx = .1
##x=0
##amplitude = 100
##for i in range (0,steps):
##    x = x + dx
##    y = amplitude*m.sin(x)
##    #print (x,y)
##    graph.setpos (x*10,y)

##scale=10
##for i in range(1,20):
##    for j in range(4):
##        graph.forward(i*scale)
##        graph.right(90)
##    graph.penup()
##    graph.forward(-.5*scale)
##    graph.left(90)
##    graph.forward(.5*scale)
##    graph.right(90)
##    graph.pendown()

##scale=10
##for i in range(1,10):
##    for j in range(3):
##        graph.forward(i*scale)
##        graph.left(120)
##    graph.penup()
##    graph.forward(-.5*scale)
##    graph.right(90)
##    graph.forward(.33*scale)
##    graph.left(90)
##    graph.pendown()

scale=40
graph.setpos(0,0)
for i in range(1,10):
    graph.right(90)
    graph.forward(8*scale)
    graph.penup()
    graph.forward(-8*scale)
    graph.left(90)
    graph.forward(1*scale)
    graph.pendown()

graph.penup()
graph.setpos(0,0)
graph.pendown()
for j in range(1,10):
    graph.forward(8*scale)
    graph.penup()
    graph.forward(-8*scale)
    graph.right(90)
    graph.forward(1*scale)
    graph.left(90)
    graph.pendown()

