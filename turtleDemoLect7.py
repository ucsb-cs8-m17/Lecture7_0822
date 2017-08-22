import turtle

t = turtle.Turtle()

def drawL(width,height):

    startX = t.xcor()
    startY = t.ycor()

    t.goto(startX,startY + height)
    t.goto(startX,startY)

    t.goto( startX + width , startY     )
    
