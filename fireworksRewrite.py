#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fireworks.py
#  
#  Copyright 2013 Devon Yard <devonyard@yahoo.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


#imports the modules we'll be using, both turtles and the random number generator
import turtle
import random

#setup the display, configures background color and exit on click
wn = turtle.Screen()
wn.bgcolor("black")

#creates all the turtles and crams them into a list
a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = [turtle.Turtle() for x in range(10)]
artists = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

#generates rotational angles and movements
m0, m1, m2, m3, m4, m5, m6, m7, m8, m9 = [random.randrange(40,60) for x in range(10)]
move = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9]
r0, r1, r2, r3, r4, r5, r6, r7, r8, r9 = [random.randrange(0,360) for x in range(10)]
rotate = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]

#Configures turtle color, I'll randomize this at some point
a0.color("Red")
a1.color("Blue")
a2.color("Purple")
a3.color("Brown")
a4.color("Gold")
a5.color("DarkKhaki")
a6.color("OrangeRed")
a7.color("DarkSlateGray")
a8.color("MediumSpringGreen")
a9.color("ForestGreen")

#set up the turtles to draw the shapes
for a in artists:
    a.speed(0)
    a.ht()
    a.penup()
    a.right(random.randrange(0,360))
    a.forward(125)
    a.pendown()

#does the actual drawing, fascinating bit of code here, it loops this sequence one-hundred and twenty times
#It calls the artists list above and pulls index 'x' from 0 to 9
#Index 'x' corresponds to a0, a1, a2 and so fourth, the turtles, but it also corresponds to the rotation and move lists
#Issues a command to a turtle, so a3.left(rotate[x])
#rotate[x] uses the same index as before, only this time it's calling the rotate list
#since the indexes correspond I can have the turtle move by a corresponding value generated for it on lines 39 and 41
for i in range(120):
    for x in range(0,9):
        artists[x].left(rotate[x])
        artists[x].forward(move[x])


wn.exitonclick()

