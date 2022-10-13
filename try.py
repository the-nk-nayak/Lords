import turtle
from sketchpy import canvas

wn=turtle.Screen()
wn.setup(width=600, height=600)

obj = canvas.sketch_from_image("ram(edited).jpg")

obj.draw()