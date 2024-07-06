from turtle import *

#we want to point a house

#step 1: draw a square

begin_fill()
width(7)
color("purple")
pendown()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(60)
color("yellow")
begin_fill()
left(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()
#end of door

#drawing a roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(130)
forward(150)
left(89)
forward(125)
end_fill()
#end of roof

#drawing a window

color("purple")
left(39)
forward(40)
color("black")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
color("purple")
forward(40)
right(90)
color("red")
forward(200)
right(90)
color("purple")
forward(38)
color("black")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end of house


exitonclick()