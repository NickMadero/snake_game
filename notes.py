import turtle
import time
import random

# create a var delay set it to .1

# create a var score and high score both set to 0

# create var window for screen
#  var window set turtle screen
# var window set to title name
# var window set to background color
# var window set to setup the width and height
# var window set to tracer(0)

# create the snake head var turtle set to turtle
# set head to speed 0
# head set shape
# head set to color
# head set to penup()
# head set to goto(num,num)
# head set to direction equals to stop

# create the food set to turtle set to turtle
# food set to speed
# food set to shape
# food set color
# food set to penup
# food set to goto(num,100)

# create var segment set to empty set

# create the var pen set to turtle set to turtle
# pen set to speed (num)
# pen set to shape(shape)
# pen set to color(color)
# pen  set to penup
# pen set to hideturtle
# pen set to goto(num,num)
# pent set to (write score = 0 high score = 0 , align equals center , font equals (Courier,24,normal))


# create function go_up
# if head direction does not equal down then head direction equals up

# create function go_down
# if head direction does not equal up then head direction equals down

# create function go_left
# if head direction does not equal right then head direction equals left

# create function go_right
# if head direction does not equal left then head direction equals right

# create function move
# if head direction double equals  up then y equals head set to ycor then head set to sety(y + 20)

# if head direction double equals down then y equals head set to ycor then head set to sety(y - 20)

# if head direction double equals left then x  equals head set to xcor then head set to setx(x - 20)

# if head direction double equals right then x equals head set to xcor then head set to setx(x + 20)


# bindings

# window set to listen
# window set to onkeypress(function go_up,w)
# window set to onkeypress(function go_down,s)
# window set to onkeypress(function go_left,a)
# window set to onkeypress(function go_right,d)

# the snake game

# while True
# window set to update

# check for collision with the borders
# if head set to xcor  > 290 or head set to xcor <- 290 or head set to ycor >290 or head set to ycor <- 290 then
# time set to sleep(1)
# head set to go to (0,0)
# head set to direction equals stop

# hide the segment
# for segment in segments then segment set to go to(1000,1000)

# clear the segments list with segments set to clear

# reset the score score equal 0

# reset the delay delay equal .1

# pen set to clear
# pen set to write( score:{} high score{} , set to format(score,high_score), align equals center, font equals( Courier, 24,normal)

# check collision with the food
# if head set to direction(food) < 20 then
# x equal to random set randint(-290,290)
# y equal to random set randint(-290,290)
#  food set to goto(x,y)

# add segment
# create new_segment equal to turtle set to turtle
# new_segment set to speed 0
# new_segment set to shape(shape)
# new_segment set to color(color)
# new_segment set to penup
# segments set to append(new_segment)

# delay minus equal .001

# score plus equal 10

# if score > high_score then
# high_score equals score

# pen set to clear
# pen set to write( score:{} high score{} , set to format(score,high_score), align equals center, font equals( Courier, 24,normal)


# move the end segments first in reverse order
# for index in range of length of segment) -1 , 0 , -1) then
# x = segments[index -1] set to xcor
# y = segments[index -1] set to ycor
# segments[index] set to goto(x,y)


# move the segment where the head is
# if length of segments > 0 then
# x = head.xcor
# y = head.ycor
# segments[index] set to goto(x,y)

# move

# check for collision with snake body

# for segment in segments then
# if segment set to distance head < 20 then
# time set to sleep 2
# head set to goto(0,0)
# head set to direction equals stop


# hide the segments
# for  segment in segments then
# segment set to goto (1000,1000)

# clear the segments list segments set to clear

# reset score score equals = 0

# reset delay delay equals = .1

# adjust the score

# pen set to clear
# pen set to write( score:{} high score{} , set to format(score,high_score), align equals center, font equals( Courier, 24,normal)

#time set to sleep display

#window set to mainloop