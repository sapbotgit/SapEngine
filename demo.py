from engine import turtleport as eng
while not eng.ready:
    pass

for i in range(10):
    eng.right()
    for a in range(i):
        eng.forward()
