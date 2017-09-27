import turtle

def draw_square(some_turtle):
	# counter = 0
	# while counter < 4:
	# 	some_turtle.forward(100)
	# 	some_turtle.right(90)
	# 	counter = counter + 1

	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():	
	window = turtle.Screen()
	window.bgcolor("black")

	# square 
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed("normal")

	for i in range (1,37): #times necessary that circle has been completly
		draw_square(brad)
		brad.right(10)

	# circule
	# angie = turtle.Turtle()
	# angie.shape("arrow")
	# angie.color("blue")
	# angie.circle(100)

	window.exitonclick()

draw_art()	