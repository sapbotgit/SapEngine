from engine import turtleport as eng
while not eng.ready:
    pass
eng.left()
for i in range(2):
    eng.forward()
    eng.right()
    eng.forward()
    eng.left()
    eng.forward()
    eng.left()
    eng.forward()
    eng.right()
eng.forward()
