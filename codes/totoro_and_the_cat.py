import turtle
import math

# Set up
window = turtle.Screen()
window.bgcolor("#496741")

cursor = turtle.Turtle()
cursor.speed(5)
cursor.pensize(3)

# Utility functions
def movePen(cursor, x, y):
  cursor.penup()
  cursor.setposition(x, y)
  cursor.pendown()

def movePenX(cursor, x):
  cursor.penup()
  cursor.setx(x)
  cursor.pendown()

def movePenY(cursor, y):
  cursor.penup()
  cursor.sety(y)
  cursor.pendown()

def positionAlongCircle(x, y, radius, angle):
  radians = math.radians(angle)
  return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

##################
# DRAW FUNCTIONS #
##################
def drawTotoro(cursor):
  cursor.color("#36302A", "#545049")

  cursor.begin_fill()

  cursor.up()
  cursor.goto(0, -200)
  cursor.right(90)
  cursor.down()

  # right side lower
  cursor.forward(4)
  cursor.circle(5, 90)
  cursor.forward(70)
  cursor.circle(130, 90)
  cursor.forward(140)
  cursor.circle(50, 20)
  cursor.circle(50, -20)
  cursor.backward(140)
  cursor.right(90)

  # right side upper
  cursor.forward(5)
  cursor.circle(20, 70)
  cursor.circle(100, 10)
  cursor.circle(500, 10)
  cursor.circle(200, 30)
  cursor.circle(3800, 3)
  cursor.right(33)
  cursor.forward(30)
  cursor.circle(100, 23)
  cursor.circle(5, 115)
  cursor.circle(200, 15)
  cursor.right(63)

  cursor.forward(130)

  # left side upper
  cursor.right(63)
  cursor.circle(200, 15)
  cursor.circle(5, 115)
  cursor.circle(100, 23)
  cursor.forward(30)
  cursor.right(33)
  cursor.circle(3800, 3)
  cursor.circle(200, 30)
  cursor.circle(500, 10)
  cursor.circle(100, 10)
  cursor.circle(20, 70)
  cursor.forward(5)

  # left side lower
  cursor.right(90)
  cursor.backward(140)
  cursor.circle(50, -20)
  cursor.circle(50, 20)
  cursor.forward(140)
  cursor.circle(130, 90)
  cursor.forward(70)
  cursor.circle(5, 90)
  cursor.forward(4)

  cursor.goto(0, -200)
  cursor.right(90)

  cursor.end_fill()

  # belly
  cursor.fillcolor("#A99881")

  cursor.begin_fill()
  cursor.circle(200)
  cursor.end_fill()

  # eyes
  rEye = 16
  rPupil = 6
  leftX = -75
  Y = 250
  movePen(cursor, leftX, Y) # left
  cursor.fillcolor("white")
  cursor.begin_fill()
  cursor.circle(rEye)
  cursor.end_fill()

  movePen(cursor, leftX, Y)
  cursor.fillcolor("black")
  cursor.begin_fill()
  cursor.circle(rPupil)
  cursor.end_fill()

  movePen(cursor, -leftX, Y) # right
  cursor.fillcolor("white")
  cursor.begin_fill()
  cursor.circle(rEye)
  cursor.end_fill()

  movePen(cursor, -leftX, Y)
  cursor.fillcolor("black")
  cursor.begin_fill()
  cursor.circle(rPupil)
  cursor.end_fill()

  # nose
  rad = 30
  movePen(cursor, -rad/2, 250)
  cursor.fillcolor("black")
  cursor.begin_fill()
  cursor.seth(-45)
  for i in range(2):
    cursor.circle(rad, 90)
    cursor.circle(rad//2, 90)
  cursor.end_fill()

  # whiskers
  length = 100
  cursor.color("black")
  # left
  movePen(cursor, -90, 230)
  cursor.setheading(180)
  cursor.forward(length)
  movePen(cursor, -95, 220)
  cursor.setheading(180)
  cursor.forward(length)
  movePen(cursor, -90, 210)
  cursor.setheading(180)
  cursor.forward(length)
  # right
  movePen(cursor, 90, 230)
  cursor.setheading(0)
  cursor.forward(length)
  movePen(cursor, 95, 220)
  cursor.setheading(0)
  cursor.forward(length)
  movePen(cursor, 90, 210)
  cursor.setheading(0)
  cursor.forward(length)


def drawCat(cursor):

  # cursor.color("#ED0A50")
  cursor.color("#36302A", "#545049")
  cursor.pensize(5)
  # head
  movePen(cursor, 0, -100)
  cursor.circle(100)

  # nose
  noseMouthOffset = -15
  movePenY(cursor, -15 + noseMouthOffset)
  cursor.fillcolor("#36302A")
  cursor.begin_fill()
  cursor.circle(15)
  cursor.end_fill()

  # Draw the mouth
  movePen(cursor, -60, -20 + noseMouthOffset)
  cursor.right(90)
  cursor.circle(30, 180)
  cursor.left(180)
  cursor.circle(30, 180)

  # eyes
  eyeSpacingX = 20
  eyePosY = 30
  eyeRadius = 20

  #right
  movePen(cursor, eyeSpacingX, eyePosY)
  cursor.right(180)
  cursor.circle(eyeRadius, -180)

  # left
  movePen(cursor, -eyeSpacingX, eyePosY)
  cursor.circle(eyeRadius, 180)

  # Right ear
  earBeginAngle = 25
  earSize = 60
  earWidth = 15
  positionA = positionAlongCircle(0, 0, 100, earBeginAngle)
  movePen(cursor, positionA[0], positionA[1])

  positionB = positionAlongCircle(0, 0, 100 + earSize, earBeginAngle + earWidth)
  cursor.setposition(positionB[0], positionB[1])

  positionC = positionAlongCircle(0, 0, 100, earBeginAngle + earWidth * 2)
  cursor.setposition(positionC[0], positionC[1])

  # Left ear
  positionA = positionAlongCircle(0, 0, 100, -earBeginAngle)
  movePen(cursor, positionA[0], positionA[1])

  positionB = positionAlongCircle(0, 0, 100 + earSize, -earBeginAngle + -earWidth)
  cursor.setposition(positionB[0], positionB[1])

  positionC = positionAlongCircle(0, 0, 100, -earBeginAngle + -earWidth * 2)
  cursor.setposition(positionC[0], positionC[1])

  # Whiskers

  whiskerLength = 120
  # Right whiskers

  movePen(cursor, 50, -15)
  cursor.setheading(0)
  cursor.forward(whiskerLength)

  movePen(cursor, 50, 0)
  cursor.left(5)
  cursor.forward(whiskerLength)

  # Left whiskers

  movePen(cursor, -50, -15)
  cursor.setheading(180)
  cursor.forward(whiskerLength)
  movePen(cursor, -50, 0)
  cursor.left(-5)
  cursor.forward(whiskerLength)

#################
# START TO DRAW #
#################

drawTotoro(cursor)
drawCat(cursor)

# Write something
movePen(cursor, 0, -150)
cursor.color("black")
cursor.write("Meow!", align="center", font=("Terminal", 30, "normal"))

movePen(cursor, 0,-270)
cursor.color("#ED0A50")
cursor.write("Totoro and the cat", 
  align="center",
  font=("Terminal", 30, "bold"))

movePen(cursor, 0, -300)
# cursor.color("#ED0A50")
cursor.color("white")
cursor.write("Reality is for people that lack imagination.",
  align="center",
  font=("Terminal", 18, "italic"))



cursor.hideturtle()
turtle.done()
