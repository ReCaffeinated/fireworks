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
window = turtle.Screen()
window.bgcolor("black")

#I still haven't found a way to automate variable creation so I'll have to do this part by hand
#Creates all the turtles
artist0 = turtle.Turtle()
artist1 = turtle.Turtle()
artist2 = turtle.Turtle()
artist3 = turtle.Turtle()
artist4 = turtle.Turtle()
artist5 = turtle.Turtle()
artist6 = turtle.Turtle()
artist7 = turtle.Turtle()
artist8 = turtle.Turtle()
artist9 = turtle.Turtle()

#Configures turtle color
artist0.color("Red")
artist1.color("Blue")
artist2.color("Purple")
artist3.color("Brown")
artist4.color("Gold")
artist5.color("DarkKhaki")
artist6.color("OrangeRed")
artist7.color("DarkSlateGray")
artist8.color("MediumSpringGreen")
artist9.color("ForestGreen")

#Sets the icon that the turtle is represented by, in this case turtle
artist0.shape("blank")
artist1.shape("blank")
artist2.shape("blank")
artist3.shape("blank")
artist4.shape("blank")
artist5.shape("blank")
artist6.shape("blank")
artist7.shape("blank")
artist8.shape("blank")
artist9.shape("blank")

#Configures speed, 1-9, with nine being the fastest, 0 even faster as it disables delay
artist0.speed(0)
artist1.speed(0)
artist2.speed(0)
artist3.speed(0)
artist4.speed(0)
artist5.speed(0)
artist6.speed(0)
artist7.speed(0)
artist8.speed(0)
artist9.speed(0)

#penup prevents them from drawing lines as they move into position
for x in[artist0,artist1,artist2,artist3,artist4,artist5,artist6,artist7,artist8,artist9]:
	x.penup()

#generates the directon the turtle faces using the random module
rotation0 = random.randrange(0,360)
rotation1 = random.randrange(0,360)
rotation2 = random.randrange(0,360)
rotation3 = random.randrange(0,360)
rotation4 = random.randrange(0,360)
rotation5 = random.randrange(0,360)
rotation6 = random.randrange(0,360)
rotation7 = random.randrange(0,360)
rotation8 = random.randrange(0,360)
rotation9 = random.randrange(0,360)

#rotates the turtle
artist0.right(rotation0)
artist1.right(rotation1)
artist2.right(rotation2)
artist3.right(rotation3)
artist4.right(rotation4)
artist5.right(rotation5)
artist6.right(rotation6)
artist7.right(rotation7)
artist8.right(rotation8)
artist9.right(rotation9)

#randomizes the length of the line cegments
move0 = random.randrange(40,60)
move1 = random.randrange(40,60)
move2 = random.randrange(40,60)
move3 = random.randrange(40,60)
move4 = random.randrange(40,60)
move5 = random.randrange(40,60)
move6 = random.randrange(40,60)
move7 = random.randrange(40,60)
move8 = random.randrange(40,60)
move9 = random.randrange(40,60)

#Moves the turtles away from the center
for x in[artist0,artist1,artist2,artist3,artist4,artist5,artist6,artist7,artist8,artist9]:
	x.forward(125)
	x.pendown()

#The turtles begin to draw
for y in range(120):
	artist0.forward(move0)
	artist1.forward(move1)
	artist2.forward(move2)
	artist3.forward(move3)
	artist4.forward(move4)
	artist5.forward(move5)
	artist6.forward(move6)
	artist7.forward(move7)
	artist8.forward(move8)
	artist9.forward(move9)
	
	artist0.left(rotation0)
	artist1.left(rotation1)
	artist2.left(rotation2)
	artist3.left(rotation3)
	artist4.left(rotation4)
	artist5.left(rotation5)
	artist6.left(rotation6)
	artist7.left(rotation7)
	artist8.left(rotation8)
	artist9.left(rotation9)

window.exitonclick()
