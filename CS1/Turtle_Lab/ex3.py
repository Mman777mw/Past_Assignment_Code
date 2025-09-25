import turtle 

# Creating Turtle
t=turtle.Turtle()
t.speed(5)
t.shape("turtle")
t.color("blue")
t.pencolor("black")

def drawXmasTree(turtle, blc, scale= 1):
	'''
	This function houses all necessary turtle processing to create the christmas tree with proper coloration for trunk, leaves, and the circle ornaments.
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

drawXmasTree(t, (100,-300), 2)
