#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fleetofartists.py
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


#imports the turtle module
import turtle
#sets up the display, turtle is the module Screen is the object and () invokes it
wn = turtle.Screen()
#calls wn which is my shorthand for window, and makes the background black
wn.bgcolor("black")

#this whole block creates the ten turtles, again turtle is the module and Turtle is the object
artist1 = turtle.Turtle()
artist2 = turtle.Turtle()
artist3 = turtle.Turtle()
artist4 = turtle.Turtle()
artist5 = turtle.Turtle()
artist6 = turtle.Turtle()
artist7 = turtle.Turtle()
artist8 = turtle.Turtle()
artist9 = turtle.Turtle()
artist10 = turtle.Turtle()

#modifies the turtles so that they don't all print the same color
artist1.color("red")
artist2.color("blue")
artist3.color("purple")
artist4.color("brown")
artist5.color("Gold")
artist6.color("DarkKhaki")
artist7.color("OrangeRed")
artist8.color("DarkSlateGray")
artist9.color("MediumSpringGreen")
artist10.color("ForestGreen")

#I put this here so that you can't se the turtles, but instead the lines they draw
artist1.shape("blank")
artist2.shape("blank")
artist3.shape("blank")
artist4.shape("blank")
artist5.shape("blank")
artist6.shape("blank")
artist7.shape("blank")
artist8.shape("blank")
artist9.shape("blank")
artist10.shape("blank")

#makes them all move as fast as possible (speed is set at 1 to 9 with 0 being faster than 9, being last on the number bar)
artist1.speed(0)
artist2.speed(0)
artist3.speed(0)
artist4.speed(0)
artist5.speed(0)
artist6.speed(0)
artist7.speed(0)
artist8.speed(0)
artist9.speed(0)
artist10.speed(0)

#with the penup command used, the artists will be able to walk around, without leaving a trail this way I can get them into position
artist1.penup()
artist2.penup()
artist3.penup()
artist4.penup()
artist5.penup()
artist6.penup()
artist7.penup()
artist8.penup()
artist9.penup()
artist10.penup()

#rather unimportant, at first there were four artists, rather than ten, so I turned them all to the cardinal directions, 2 was already facing right, as they spawn that way, so I didn't change it
artist1.left(90)
artist3.right(90)
artist4.right(180)
#brings in the random number generator, a module that generates random numbers, imagine that
import random

#sets values that I later used for rotation, did the same thing as the .left and right modifiers on artists 1-4, this way it was more spontaneous
#I don't know why I used 1 through 361 rather than 0 through 360, I guess I'm just stupid like that
a = random.randrange(1,361)
b = random.randrange(1,361)
c = random.randrange(1,361)
d = random.randrange(1,361)
e = random.randrange(1,361)
f = random.randrange(1,361)
#this passes the generated number on to the turtles so they can rotate that way
artist5.right(a)
artist6.right(b)
artist7.right(c)
artist8.right(d)
artist9.right(e)
artist10.right(f)

#another remnant of my dumbassery, I used words meaning rotate for the first four, which was all I had in the original version of this script, then when I added the other six I scrapped that
#these variables tell them how far to walk from the center, makes them show up in a different position each time
turn = random.randrange(45,180)
twist = random.randrange(45,180)
rotate = random.randrange(45,180)
spin = random.randrange(45,180)
t1 = random.randrange(45,180)
t2 = random.randrange(45,180)
t3 = random.randrange(45,180)
t4 = random.randrange(45,180)
t5 = random.randrange(45,180)
t6 = random.randrange(45,180)

#I did the same thing here, the name of the variable isn't important, the damn thing works
move = random.randrange(40,60)
walk = random.randrange(40,60)
shuffle = random.randrange(40,60)
scuttle = random.randrange(40,60)
w1 = random.randrange(40,60)
w2 = random.randrange(40,60)
w3 = random.randrange(40,60)
w4 = random.randrange(40,60)
w5 = random.randrange(40,60)
w6 = random.randrange(40,60)

#for the longest time I couldn't remember what this even did, I had to look it up
#this runs ten times and each time it replaces x with an artist1 or artist2, corresponding to the run it's on, they walk forward 125 units and start writing when they get there
#come to think of it why didn't I do this with the other variables 
#I just went back and checked and I STILL DON'T DO THIS WITH CODE I WRITE NOW, I AM NOT A SMART MAN
for x in[artist1,artist2,artist3,artist4,artist5,artist6,artist7,artist8,artist9,artist10]:
	x.forward(125)
	x.pendown()
#this loop is set to run 120 times, the y is unimportant, it uses the walk and rotate values set earlier, which I wrote again, and again, rather than automating with a loop like this one
#HURR DURR, LET'S TYPE MORE
for y in range(120):
	artist1.forward(move)
	artist2.forward(walk)
	artist3.forward(shuffle)
	artist4.forward(scuttle)
	artist5.forward(w1)
	artist6.forward(w2)
	artist7.forward(w3)
	artist8.forward(w4)
	artist9.forward(w5)
	artist10.forward(w6)
	
	artist1.left(turn)
	artist2.left(twist)
	artist3.left(rotate)
	artist4.left(spin)
	artist5.left(t1)
	artist6.left(t2)
	artist7.left(t3)
	artist8.left(t4)
	artist9.left(t5)
	artist10.left(t6)

#makes the screen close when clicked
wn.exitonclick()
