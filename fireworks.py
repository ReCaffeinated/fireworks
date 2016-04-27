#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
import random
#setup the display, configures background color
wn = turtle.Screen()
wn.bgcolor("black")

#creates all the turtles and crams them into a list
artists = [turtle.Turtle() for x in range(10)]
#generates rotational angles and movements
move = [random.randrange(40,60) for x in range(10)]
rotate = [random.randrange(0,360) for x in range(10)]

#Configures turtle color
colors = (
"Red","Blue","Purple","Brown","Gold",
"DarkKhaki","OrangeRed","DarkSlateGray",
"MediumSpringGreen","ForestGreen"
)
for artist, color in zip(artists, colors):
	artist.color(color)

#set up the turtles to draw the shapes
for a in artists:
    a.speed(0)
    a.ht()
    a.penup()
    a.right(random.randrange(0,360))
    a.forward(125)
    a.pendown()
for i in range(120):
    for x in range(0,9):
        artists[x].left(rotate[x])
        artists[x].forward(move[x])
wn.exitonclick()
