import turtle

# Creating Turtle
t = turtle.Turtle()
t.speed(1)

def drawHouse(turtle, blc, scale = 1):
	'''
	Creating a house made of a square with a triangle roof and rectangle door with circular knob.
	Instructor Comments:
	'''
	turtle.goto(blc)
	turtle.right(90)
	squareLength = 50 * scale
	
	for x in range(4):
	
		turtle.forward(squareLength)
		turtle.left(90)

	#Creating triangle.
	triangleLength = 35.5 * scale
	turtle.setheading(45)
	turtle.forward(triangleLength)
	turtle.right(90)
	turtle.forward(triangleLength)
	turtle.right(45)
	turtle.forward(squareLength)
	turtle.right(90)
	turtle.forward(squareLength/2)

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
	turtle.left(90)
	turtle.up()
	turtle.forward(doorLength // 2.5)
	turtle.down()
	turtle.circle(1 * scale)

	# Window Setup
	handleToWindowDistance = 10 * scale
	turtle.right(90)
	turtle.up()
	turtle.forward(handleToWindowDistance)
	turtle.down()
	turtle.left(90)

	# Window Square Size
	windowLength = 10 * scale
	for windows in range(4):

		turtle.forward(windowLength)
		turtle.right(90)

	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength)
	turtle.right(90)
	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength // 2)
	turtle.right(90)
	turtle.forward(windowLength)


drawHouse(t, (0,0), 5)
