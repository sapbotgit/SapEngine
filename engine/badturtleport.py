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
    for i in range(3):
        t.left(90)
def backward():
    for i in range(2):
        t.left(90)
    t.forward(step)
    for i in range(2):
        t.left(90)
window.title('SapEngine: badturtleport')
window.setup(WIDTH, HEIGHT)
ready = True
