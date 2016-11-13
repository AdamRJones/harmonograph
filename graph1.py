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


# squares
scale=10
for i in range(1,10):
    for j in range(4):
        graph.forward(i*scale)
        graph.right(90)
    graph.penup()
    graph.forward(-.5*scale)
    graph.left(90)
    graph.forward(.5*scale)
    graph.right(90)
    graph.pendown()


# move pen
graph.penup()
graph.setpos(200,0)
graph.pendown()


# triangles
scale=10
for i in range(1,10):
    for j in range(3):
        graph.forward(i*scale)
        graph.left(120)
    graph.penup()
    graph.forward(-.5*scale)
    graph.right(90)
    graph.forward(.33*scale)
    graph.left(90)
    graph.pendown()


# move pen
graph.penup()
graph.setpos(-200,50)
graph.pendown()


# chessboard
scale=10
for i in range(1,10):
    graph.right(90)
    graph.forward(8*scale)
    graph.penup()
    graph.forward(-8*scale)
    graph.left(90)
    graph.forward(1*scale)
    graph.pendown()

graph.penup()
graph.setpos(-200,50)
graph.pendown()

for j in range(1,10):
    graph.forward(8*scale)
    graph.penup()
    graph.forward(-8*scale)
    graph.right(90)
    graph.forward(1*scale)
    graph.left(90)
    graph.pendown()

