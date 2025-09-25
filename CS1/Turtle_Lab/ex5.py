import turtle 

# Creating Turtle
t=turtle.Turtle()
t.speed(5)
t.shape("turtle")
t.color("blue")
t.pencolor("black")

def main():
	'''
	The main function that executes everything.
	Also contains instructions, that are printed in the idle window, for modifying placement and scale for the various images in the scene.
	'''
	winterScene(t)	# main function will execute winterscene
	print("To change position and scale: \nOpen python file for this program.\nGo to the function for the item you want to edit.\nfunctionExample(t, (x,y), s)")
	print('"t" is your turtle. LEAVE THAT ALONE!! ... unless you want the program to not work.\n"(x,y)" is your x and y coordinates for positioning.\n"s" is your scale.(Bigger < 1 ; Smaller 1 > "s" > 0\nThere you go.\nHave fun and go nuts.')

def winterScene(t):	# Required function for assignment. Normally would use main to function to perform this task.
	# Utilizing functions from ex2, ex3, and ex4 as they are components of this assignment.
	# Scale and bottom left corner used for positioning and sizing in scene.
	'''
	Main govenor of all the functions in the program.
	Editing function values here allows for position and scale to be modified.
	'''

	drawHouse(t, (50,10), 4)
	drawXmasTree(t, (-100,-200), 1.5)
	drawSnowMan_main(t, (300, -200), 2.5)


def drawHouse(turtle, blc, scale = 1):	# Function for creating house. Modified from ex2 to add color to house.
	'''
	Creating a house made of a square with a triangle roof and rectangle door with circular knob.
	Instructor Comments:
	'''
	turtle.up()
	turtle.goto(blc)
	turtle.down()
	turtle.right(90)
	squareLength = 50 * scale
	turtle.pencolor("brown")
	turtle.fillcolor("brown")
	turtle.begin_fill()
	for x in range(4):
	
		turtle.forward(squareLength)
		turtle.left(90)

	turtle.end_fill()
	turtle.pencolor("blue")
	turtle.fillcolor("blue")
	turtle.begin_fill()
	#Creating triangle.
	triangleLength = 35.5 * scale
	turtle.setheading(45)
	turtle.forward(triangleLength)
	turtle.right(90)
	turtle.forward(triangleLength)
	turtle.right(45)
	turtle.end_fill()
	turtle.forward(squareLength)
	turtle.right(90)
	turtle.forward(squareLength/2)

	turtle.pencolor("black")
	turtle.fillcolor("red")
	turtle.begin_fill()
	#Door & handle
	doorLength = 25 * scale
	turtle.setheading(90)
	turtle.forward(doorLength)
	turtle.left(90)
	turtle.forward(doorLength // 2.5)
	turtle.left(90)
	turtle.forward(doorLength)
	turtle.left(90)
	turtle.forward(doorLength // 3)
	turtle.end_fill()
	turtle.left(90)
	turtle.up()
	turtle.pencolor("black")
	turtle.fillcolor("gold")
	turtle.forward(doorLength // 2.5)
	turtle.down()
	turtle.begin_fill()
	turtle.circle(1 * scale)
	turtle.end_fill()

	# Window Setup
	turtle.fillcolor("white")
	handleToWindowDistance = 10 * scale
	turtle.right(90)
	turtle.up()
	turtle.forward(handleToWindowDistance)
	turtle.down()
	turtle.begin_fill()
	turtle.left(90)

	# Window Square Size
	windowLength = 10 * scale
	for windows in range(4):

		turtle.forward(windowLength)
		turtle.right(90)

	turtle.end_fill()
	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength)
	turtle.right(90)
	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength)


def drawXmasTree(turtle, blc, scale= 1): # Function for creating christmas tree. Brought in from ex3 because copy and paste is your friend. :3
	'''
	Function creating the christmas tree with ornament.
	'''
	turtle.up()
	turtle.goto(blc)
	turtle.down()
	turtle.right(90)
	#Creating the trunk
	trunkLength = 100 * scale
	turtle.pencolor("brown")
	turtle.fillcolor("brown")
	turtle.begin_fill()
	turtle.setheading(90)
	turtle.forward(trunkLength/1.5)
	turtle.left(90)
	turtle.forward(trunkLength)
	turtle.left(90)
	turtle.forward(trunkLength/1.5)
	turtle.left(90)
	turtle.forward(trunkLength)
	turtle.left(90)
	turtle.forward(trunkLength/1.5)
	turtle.left(90)
	turtle.end_fill()

	#creating triangles for leaves
	triangleLarge = trunkLength * 2
	

	turtle.pencolor("green")
	turtle.fillcolor("green")
	turtle.begin_fill()
	turtle.forward(trunkLength /2)
	turtle.forward(trunkLength*1.4)
	turtle.setheading(45)
	turtle.forward(triangleLarge)
	turtle.right(90)
	turtle.forward(triangleLarge)
	turtle.setheading(180)
	turtle.forward(triangleLarge*1.4)
	turtle.end_fill()
	turtle.right(45)

	turtle.up()
	turtle.right(115)
	turtle.forward(triangleLarge/1.4)
	turtle.down()
	turtle.begin_fill()
	turtle.setheading(180)
	turtle.forward(triangleLarge/1.4)
	turtle.setheading(45)
	turtle.forward(triangleLarge)
	turtle.right(90)
	turtle.forward(triangleLarge)
	turtle.setheading(180)
	turtle.forward(triangleLarge*1.4)
	turtle.end_fill()
	turtle.right(45)

	turtle.up()
	turtle.right(115)
	turtle.forward(triangleLarge/1.4)
	turtle.down()
	turtle.begin_fill()
	turtle.setheading(180)
	turtle.forward(triangleLarge/1.4)
	turtle.setheading(45)
	turtle.forward(triangleLarge)
	turtle.right(90)
	turtle.forward(triangleLarge)
	turtle.setheading(180)
	turtle.forward(triangleLarge*1.4)
	turtle.end_fill()

	#the ball on top
	
	turtle.pencolor("black")
	turtle.fillcolor("yellow")
	turtle.up()
	turtle.setheading(45)
	turtle.forward(triangleLarge)
	turtle.down()
	turtle.begin_fill()
	turtle.circle(25 * scale)
	turtle.end_fill() 

def drawSnowMan_main(turtle, blc, scale):
	'''
	Main function for the snowman in ex4.
	Some minor alterations were necessary to make things play nice with the winterscene function.
	Mainly only exists to govern the subfuntions for the snowman in the winter scene function in one place.
	'''

	#   Starting Point
	turtle.up()
	turtle.goto(blc)
	turtle.setheading(0)
	turtle.down()

	drawSnowMan(t, scale)
	snowmanHat(t, scale)
	snowmanFacialDecoration(t, scale)
	snowmanNoseMouth(t, scale)
	centerMassArmsFingers(t, scale) 

def drawSnowMan(cursor, 
                scale=1, firstCircle=15, 
                secondCircle=12.5, thirdCircle=10):
    '''
    Draws Foundation Of Snowman (Circles)
    Instructors Comments:
    '''

    
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


def snowmanHat(cursor, scale=1):
    '''
    Draws Hat Of Snowman (Rectangle & Square)
    Instructors Comments:
    '''
    #   Scaling Point
    rectangleLength=20 * scale
    rectangleWidth=5 * scale
    squareSize=10 * scale

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
    
    
def snowmanFacialDecoration(cursor, scale=1):
    '''
    Draws Facial Decoration Of Snowman
    Instructors Comments:
    '''
    #   Scaling Point
    rectangleWidth=5 * scale
    thirdCircle=10 * scale
    eyeCircles=1.5 * scale
    eyeCircles=1.5 * scale
    eyeDistance=5 * scale
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
    cursor.forward(eyeDistance)
    cursor.down()

    #   Left Eye Starting Position
    cursor.fillcolor('black')
    cursor.begin_fill()
    cursor.right(60)
    cursor.circle(eyeCircles)
    cursor.end_fill()


def snowmanNoseMouth(cursor, scale=1):
    '''
    Draws Distance from Left Eye to Bottom Left Corner of Mouth
    Instructors Comments:
    '''
    #   Scaling Point 
    mouthLength=10 * scale
    triangleNoseLengths=5 * scale
    eyetonoseDistance=3 * scale
    mouthtoCenterMass=20 * scale
    
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
    
    
def centerMassArmsFingers(cursor, scale=1):
    '''
    This Function Creates Two Appropiately Porportioned Arms & Fingers On The Snowman
    Instructors Comments: 
    '''
    #   Scaling Point
    armLength=40 * scale
    fingerLength=10 * scale
    
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


if __name__ == "__main__":	#using a main function to execute winterscene function
	main()
