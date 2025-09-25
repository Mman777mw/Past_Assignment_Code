import turtle
import math

#	Creating Turtle Object
t = turtle.Turtle()
t.speed(1)

# Establishing PI
pie = math.pi

def drawCircleA(t, centerpoint, radius):
	'''
	Calculate distance with formula 2.0 * pi * radius/ 120.0
	The turtle should draw a circumference of the circle by turning 3 degrees and moving 120 times a given distance.
	'''
	t.up()
	t.goto(centerpoint)
	
	t.forward(radius)
	t.down()
	
	t.left(90)
	for x in range(121):
		
		t.left(3)
		t.forward((radius*2*pie)/120)

		
	distanceMoved = (2.0* pie * radius)/120
	print(f"The turtle moved {distanceMoved}.")
	return distanceMoved
	

drawCircleA(t, (0,0), 40)
