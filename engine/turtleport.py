import turtle as tsrc
ready = False
tsrc.speed(0)
window = tsrc.Screen()
t = tsrc.Turtle()
W, H = input('Ширина экрана >'), input('Высота экрана >')
WIDTH, HEIGHT = int(W), int(H)
step = HEIGHT / 10
def forward():
    t.forward(step)
def left():
    t.left(90)
def right():
    t.right(90)
def backward():
    t.backward(step)
window.title('SapEngine: turtleport')
window.setup(WIDTH, HEIGHT)
ready = True
