import turtle
import time

SIZE = 8
SPEED = 8
STEPS = 280

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("white")
screen.title("Анииация человека")
screen.tracer(0)

man = turtle.Turtle()
man.speed(0)
man.penup()
man.hideturtle()
man.pensize(2)

def scale(v):
    return v * SIZE

def draw_man(x, y):
    man.clear()
    man.color("black")
    head_center_x = x
    head_center_y = y + scale(80)
    radius = scale(25)
    man.goto(head_center_x, head_center_y - radius)
    man.pendown()
    man.circle(radius)
    man.penup()
    man.goto(head_center_x - scale(10), head_center_y + scale(5))
    man.pendown()
    man.dot(scale(5))
    man.penup()
    man.goto(head_center_x + scale(10), head_center_y + scale(5))
    man.pendown()
    man.dot(scale(5))
    man.penup()
    man.goto(head_center_x - scale(10), head_center_y - scale(8))
    man.pendown()
    man.forward(scale(20))
    man.penup()
    neck_y = head_center_y - radius
    waist_y = y + scale(30)
    man.goto(x, neck_y)
    man.pendown()
    man.goto(x, waist_y)
    man.penup()
    shoulder_y = neck_y
    man.goto(x, shoulder_y)
    man.pendown()
    man.goto(x - scale(35), waist_y - scale(10))
    man.penup()
    man.goto(x, shoulder_y)
    man.pendown()
    man.goto(x + scale(35), waist_y - scale(10))
    man.penup()
    man.goto(x, waist_y)
    man.pendown()
    man.goto(x - scale(30), y)
    man.penup()
    man.goto(x, waist_y)
    man.pendown()
    man.goto(x + scale(30), y)
    man.penup()

    screen.update()

x_pos = 0
direction = -1

while True:
    x_pos += SPEED * direction
    if x_pos <= -STEPS:
        direction = 1
    elif x_pos >= STEPS:
        direction = -1

    draw_man(x_pos, 50)
    time.sleep(0.04)

turtle.done()