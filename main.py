import random
from turtle import Turtle, Screen

list_of_turtle_colors = ['red','green','blue','yellow','violet', 'orange']
list_of_turtles = []

x=-200
y=150
for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(list_of_turtle_colors[i])
    new_turtle.penup()
    new_turtle.goto(x,y)
    y -= 50
    list_of_turtles.append(new_turtle)

screen = Screen()
screen.setup(width=500, height=400)
user_selection_of_turtle = screen.textinput(title='Make your bet', prompt="Select the turtle for victory from 'red','green','blue','yellow','violet', 'orange'")


winner_turtle = ''
j = True
while j is True:
    random_lenght = random.randrange(0,10)
    random_turtle = random.randrange(0,6)
    moving_turtle = list_of_turtles[random_turtle]
    moving_turtle.forward(random_lenght)
    position_of_the_turtle = moving_turtle.position()
    if position_of_the_turtle[0] >= 220:
        winner_turtle = moving_turtle
        j = False

s = 0
winning_color = ''
for s in range(0,6):
    if list_of_turtles[s] == winner_turtle:
        winning_color = list_of_turtle_colors[s]
print(winner_turtle)
if user_selection_of_turtle == winner_turtle:
    print(f'You selected {user_selection_of_turtle} turtle')
    print(f'Wow! You got it right! {winning_color} turtle won')
else:
    print(f'You selected {user_selection_of_turtle} turtle')
    print(f'Ha! Loser! {winning_color} turtle was the best!')


screen.exitonclick()