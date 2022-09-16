import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#tracer basically stops the window from updating allowing the game to be faster
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# goto sets up with coordinates of paddle_a (x,y)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Score 
score_a = 0
score_b = 0
pt_to_a = 0
pt_to_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))



# Function
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




# Main Game Loop
while True:
  wn.update()

  # Move the ball
  if pt_to_a > 1:
    pt_to_a = 0
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
  elif pt_to_b > 1:
    pt_to_b = 0
    ball.setx(ball.xcor() - ball.dx)
    ball.sety(ball.ycor() - ball.dy)
  else:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


  # Border checking
  # The reason ball.dy/ball.dx is negative for all xcor and ycor statements is b/c it reverses the direction once it reaches a certain x/y cord as dy/dx * (-) reverses direction (current dx/dy created above being 0.5)
  # Ex: ball.dy *= -1 -> ball.dy = ball.dy * -0.25 -> ball.dy = 0.5 * -1
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.setx(390)
    ball.dx *= -1
    winsound.PlaySound("score.wav", winsound.SND_ASYNC)
    score_a += 1
    pt_to_a += 1
    ball.goto(0,0)
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

  
  if ball.xcor() < -390:
    ball.setx(-390)
    ball.dx *= -1
    winsound.PlaySound("score.wav", winsound.SND_ASYNC)
    score_b += 1
    pt_to_b += 1
    ball.goto(0,0)
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))


  # Paddle and ball connect
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    ball.setx(-340)
    ball.dx *= -1

  if (score_a == 5 or score_b == 5):
    for t in wn.turtles():
      t.reset()
    winner = turtle.Turtle()
    winner.speed(0)
    winner.color("white")
    winner.penup()
    winner.hideturtle()
    winner.goto(0,0)
    if score_a == 5:
      winner.write("Player A wins", align="center", font=("Courier", 18, "normal"))
      winner.goto(0, -25)
      winner.write("Mouse click to exit!", align="center", font=("Courier", 18, "normal"))
    else:
      winner.write("Player B wins", align="center", font=("Courier", 18, "normal"))
      winner.goto(0, -25)
      winner.write("Mouse click to exit!", align="center", font=("Courier", 18, "normal"))
    wn.exitonclick()
    
 
  
 



