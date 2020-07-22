import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#17bee3")
t.speed(10)

def triangle(size):
	for i in range(3):
		t.rt(size)
		t.fd(100)
triangle(120)