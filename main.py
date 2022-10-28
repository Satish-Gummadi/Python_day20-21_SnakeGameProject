# snake game project using python turtle module (python day 20)

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

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

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)




screen.exitonclick()
