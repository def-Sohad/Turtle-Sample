import turtle
window = turtle.Screen()
window.bgcolor('black')

sohad = turtle.Turtle()
sohad.shape('square')
sohad.pensize(10)
sohad.speed(7)
sohad.color('black')
sohad.left(180)
sohad.forward(300)
sohad.right(90)
sohad.forward(100)
sohad.right(90)
sohad.color('gold')

direction = 30
road = 60

for _ in range(15):
    sohad.right(direction)
    sohad.forward(road)
for _ in range(18):
    sohad.left(30)
    sohad.forward(60)
for _ in range(18):
    sohad.right(30)
    sohad.forward(60)
for _ in range(15):
    sohad.left(30)
    sohad.forward(60)
window.exitonclick()
print('                When Ever You See Audi')
print('             Do Not think about other Cars')
print('                  Now you Understand')
