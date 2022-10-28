# snake game project using python turtle module (python day 20)

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# turtle_size = []
# x_position = 0
#
# for i in range(3):
#     block = Turtle('square')
#     block.color('white')
#     block.setpos(x=x_position,y=0)
#     turtle_size.append(block)
#     x_position = x_position - 20


starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# to move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for seg_num in range(len(segments)-1,0,-1):
        x_cor = segments[seg_num - 1].xcor()
        y_cor = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x_cor,y_cor)

    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
