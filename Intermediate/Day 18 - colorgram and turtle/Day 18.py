import turtle as t
import colorgram
import random

"""
colors = colorgram.extract('hirst.jpg', 108)
color_palette = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_c = (r, g, b)
    color_palette.append(new_c)

print(color_palette)
"""

screen = t.Screen()
t.colormode(255)
brush = t.Turtle()
brush.speed("fastest")

brush.penup()
brush.goto(-350, 350)

color_palette = [(240, 233, 227), (226, 238, 229), (242, 229, 234), (225, 233, 240), (208, 150, 111), (156, 76, 46), (48, 99, 139), (230, 210, 104), (143, 68, 93), (133, 168, 194), (204, 132, 153), (59, 117, 66), (131, 188, 159), (205, 85, 107), (219, 84, 55), (18, 44, 76), (61, 171, 104), (65, 43, 29), (161, 208, 191), (35, 54, 114), (235, 173, 159), (133, 39, 27), (230, 167, 181), (110, 42, 61), (158, 205, 213), (197, 124, 49), (61, 39, 47), (39, 62, 43), (38, 81, 51), (73, 71, 40), (69, 154, 168), (122, 111, 163), (179, 185, 215), (13, 82, 102), (249, 207, 1)]

  
for i in range(15):
    for i in range(15):
        brush.dot(20, random.choice(color_palette))
        brush.forward(50)
    brush.right(90)
    brush.forward(50)
    brush.right(90)
    brush.forward(750)
    brush.right(180)
    




