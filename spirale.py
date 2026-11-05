import turtle

ecran = turtle.Screen()
ecran.bgcolor("black")
ecran.title("Spiral Art")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

couleurs = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

for i in range(120):
    t.color(couleurs[i % len(couleurs)])
    t.forward(i * 2)
    t.left(59)

turtle.done()