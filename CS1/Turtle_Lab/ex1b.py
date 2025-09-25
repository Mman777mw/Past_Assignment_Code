import turtle

john_the_turtle = turtle.Turtle()

def circleFunction(T, scale):
    '''
    Drawing a circle using built in .circle() method rather than creating your own method from scratch.
    '''
    
    T.home()
    T.circle(scale)
    
circleFunction(john_the_turtle, 100)
