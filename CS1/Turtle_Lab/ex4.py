import turtle


t = turtle.Turtle()
t.speed(2)

def drawSnowMan(cursor, blc, 
                scale=1, firstCircle=15, 
                secondCircle=12.5, thirdCircle=10):
    '''
    Draws Foundation Of Snowman (Circles)
    Instructors Comments:
    '''
    #   Starting Point
    cursor.up()
    cursor.goto(blc)
    cursor.down()
    
    #   Scaling Point
    firstCircle *= scale
    secondCircle *= scale
    thirdCircle *= scale
    
    #   First Circle
    cursor.fillcolor('white')
    cursor.begin_fill()
    cursor.circle(firstCircle)
    cursor.end_fill()
    
    #   Vertical Movement From Circle Starting Point -> Towards Next Circles Starting point
    cursor.up()
    cursor.left(90)
    cursor.forward(firstCircle * 2)
    cursor.right(90)
    cursor.down()
    
    #   Second Circle
    cursor.fillcolor('white')
    cursor.begin_fill()
    cursor.circle(secondCircle)
    cursor.end_fill()
    
    #   Vertical Movement From Circle Starting Point -> Towards Next Circles Starting point
    cursor.up()
    cursor.left(90)
    cursor.forward(secondCircle * 2)
    cursor.right(90)
    cursor.down()

    #   Third Circle
    cursor.fillcolor('white')
    cursor.begin_fill()
    cursor.circle(thirdCircle)
    cursor.end_fill()

    #   Jumps From Bottom of Top Circle To Top of Circles   
    cursor.up()
    cursor.left(90)
    cursor.forward(thirdCircle * 2)
    cursor.right(90)
    cursor.down()


def snowmanHat(cursor, rectangleLength=20, 
               rectangleWidth=5, squareSize=10, 
               scale=1):
    '''
    Draws Hat Of Snowman (Rectangle & Square)
    Instructors Comments:
    '''
    #   Scaling Point
    rectangleLength *= scale
    rectangleWidth *= scale
    squareSize *= scale

    #   Top Center Of SnowMan Circles
    #   Hat Starting Position IN MEMORY
    
    #   Builds Base of Hat
    cursor.fillcolor('black')
    cursor.begin_fill()
    cursor.forward(rectangleLength / 2)
    cursor.left(90)
    cursor.forward(rectangleWidth)
    cursor.left(90)
    cursor.forward(rectangleLength)
    cursor.left(90)
    cursor.forward(rectangleWidth)
    cursor.left(90)
    cursor.end_fill()

    #   Travel Route To Square Starting Point
    cursor.forward(rectangleLength)
    cursor.left(90)
    cursor.forward(rectangleWidth)
    cursor.left(90)
    cursor.forward(rectangleLength / 4)
    cursor.right(90)
    
    #   Square Starting Point, Completion, & Coloring 
    cursor.fillcolor('black')
    cursor.begin_fill()
    for _ in range(0, 4, 1):
        
        cursor.forward(squareSize)
        cursor.left(90)
    cursor.end_fill()
    
    
def snowmanFacialDecoration(cursor, scale=1, 
                            rectangleWidth=5, thirdCircle=10, 
                            eyeCircles=1.5, eyeDistance=10):
    '''
    Draws Facial Decoration Of Snowman
    Instructors Comments:
    '''
    #   Scaling Point
    rectangleWidth *= scale
    thirdCircle *= scale
    eyeCircles *= scale

    #   Movement From Bottom Right Corner of Square -> Right Eye Positioning
    cursor.pencolor('black')
    cursor.up()
    cursor.right(180)
    cursor.forward(rectangleWidth * 2)
    cursor.right(90)
    cursor.forward(thirdCircle/ 2.2)
    cursor.left(90)

    cursor.down()
    
    #   Right Eye Starting Position
    cursor.fillcolor('black')
    cursor.begin_fill()
    cursor.circle(eyeCircles)
    cursor.end_fill()

    #  Mid Eye Distance Split
    cursor.up()
    cursor.setheading(180)
    cursor.forward(eyeDistance * 2)
    cursor.down()

    #   Left Eye Starting Position
    cursor.fillcolor('black')
    cursor.begin_fill()
    cursor.right(60)
    cursor.circle(eyeCircles)
    cursor.end_fill()


def snowmanNoseMouth(cursor, scale=1,
                 eyetonoseDistance=3, mouthLength=10, 
                 triangleNoseLengths=5, mouthtoCenterMass=70):
    '''
    Draws Distance from Left Eye to Bottom Left Corner of Mouth
    Instructors Comments:
    '''
    #   Scaling Point 
    mouthLength *= scale
    triangleNoseLengths *= scale
    eyetonoseDistance *= scale
    
    #  Left Eye To Bottom Left Corner of Nose
    cursor.up()
    cursor.right(180)
    cursor.forward(eyetonoseDistance)
    cursor.down()
    
    #   Nose
    cursor.pencolor('orange')
    cursor.fillcolor('orange')
    cursor.begin_fill()
    cursor.left(45)
    cursor.forward(triangleNoseLengths)
    cursor.right(125) 
    cursor.forward(triangleNoseLengths)
    cursor.right(125)
    cursor.end_fill()
    cursor.forward(triangleNoseLengths)
    cursor.right(150)
    
    
    #   Travel to Mouth Starting Spot
    cursor.up()
    cursor.pencolor('black')
    cursor.forward(mouthLength* .8)
    cursor.down()
    
    
    #   Completion of Mouth
    cursor.left(45)
    cursor.forward(mouthLength // 2)
    cursor.left(180)
    cursor.forward(mouthLength)
    cursor.left(180)
    cursor.forward(mouthLength // 2)
    cursor.right(105)
    
    #   Move to Center Mass From Mouth
    cursor.up()
    cursor.forward(mouthtoCenterMass)
    cursor.right(90)
    cursor.down()
    
    
def centerMassArmsFingers(cursor, scale=1, 
                          armLength=40, fingerLength=10):
    '''
    This Function Creates Two Appropiately Porportioned Arms & Fingers On The Snowman
    Instructors Comments: 
    '''
    #   Scaling Point
    armLength *= scale
    fingerLength *= scale
    
    #   Starting Center Mass
    cursor.forward(armLength // 2)
    
    
    #   Left Arm Fingers
    cursor.left(45)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(125)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(90)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(115)
    cursor.up()
    cursor.right(15)
    cursor.forward(fingerLength)
    
    #   Travel from Center Left Hand to Right Hand
    #   Completion of Right Hand
    cursor.up()
    cursor.forward(armLength / 2)
    cursor.down()
    
    cursor.forward(armLength // 2)
    
    cursor.left(45)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(125)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(90)
    cursor.forward(fingerLength)
    cursor.right(180)
    cursor.forward(fingerLength)
    cursor.left(45)



def main():
    
    drawSnowMan(t, (0, -200), 6)
    snowmanHat(t, scale=6)
    snowmanFacialDecoration(t, scale=6)
    snowmanNoseMouth(t, scale=6)
    centerMassArmsFingers(t, scale=6) 

if __name__ == '__main__':

    main()
